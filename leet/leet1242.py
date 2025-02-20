from urllib.parse import urlparse
import threading

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
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
