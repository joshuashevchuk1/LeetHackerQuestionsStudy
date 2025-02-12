from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from threading import Lock

def concurrentUrlDownload(urls, k):
    result = {}
    result_lock = Lock()

    def getUrl(url):
        response = requests.get(url)
        if response.status_code == 200:
            with result_lock:
                result[url] = response.content
        else:
            raise Exception(f"Failed: {url} (status code {response.status_code})")

    def cycle(urls):
        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(getUrl, url): url for url in urls}

            for future in as_completed(futures):
                future.result()

    cycle(urls, batchSize=k)
    return result

file_url = "https://www.sample-videos.com/img/Sample-jpg-image-50kb.jpg"
urls = (file_url for _ in range(5))

result = concurrentUrlDownload(urls, k=2)
print(len(result))
