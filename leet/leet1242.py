from urllib.parse import urlparse
import threading

from urllib.parse import urlparse
import threading
from concurrent.futures import ThreadPoolExecutor
from queue import Queue


class SolutionButThreadSafe:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> list[str]:
        host = urlparse(startUrl).netloc  # Extract base domain
        visited = set()
        queue = Queue()
        queue.put(startUrl)
        lock = threading.Lock()

        def getUrl():
            while True:
                url = queue.get()
                if url is None:  # Exit signal for workers
                    break

                with lock:
                    if url in visited:
                        queue.task_done()
                        continue
                    visited.add(url)

                for new_url in htmlParser.getUrls(url):
                    if urlparse(new_url).netloc == host:  # Ensure same domain
                        with lock:
                            if new_url not in visited:
                                queue.put(new_url)

                queue.task_done()

        num_workers = 10
        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            workers = [executor.submit(getUrl) for _ in range(num_workers)]

            queue.join()  # Wait for all tasks to be processed

            for _ in range(num_workers):  # Send exit signals to workers
                queue.put(None)

        return list(visited)


class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> list[str]:
        host = urlparse(startUrl).netloc
        visited = set()
        mutex = threading.Lock()
        threads = []

        def getUrl(url):
            with mutex:
                if url in visited:
                    return
                visited.add(url)

            urls = htmlParser.getUrls(url)
            for link in urls:
                if urlparse(link).netloc == host:
                    with mutex:
                        if link not in visited:
                            thread = threading.Thread(target=getUrl, args=(link,))
                            thread.start()
                            threads.append(thread)

        initial_thread = threading.Thread(target=getUrl, args=(startUrl,))
        initial_thread.start()
        threads.append(initial_thread)

        for thread in threads:
            thread.join()

        return list(visited)
