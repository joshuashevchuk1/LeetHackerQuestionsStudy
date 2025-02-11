def solve(n):

    def getUrl(url,filename):
        response = requests.get(url)
        if response.status_code == 200:
            with open(str(filename),"wb") as f:
                f.write(response.content)
        else:
            raise Exception("status code is not 200")


    def mapURLS(urlList):
        with ThreadPoolExecutor() as exec:
            for i in range(len(urlList)):
                exec.submit(getUrl,urlList[i],str(i) + ".jpg")

    def getUrlList(number):
        urlList = ["https://www.sample-videos.com/img/Sample-jpg-image-50kb.jpg" for i in range(number)]
        return urlList

    def process(n):
        url_list = getUrlList(n)
        mapURLS(url_list)

    process(n)

#solve(20)

from concurrent.futures import ThreadPoolExecutor
import requests

def solveFull(n):
    # Function to fetch data from URL
    def getUrl(url):
        response = requests.get(url)
        if response.status_code == 200:
            return int(response.text)  # Assuming the content is a number in text format
        else:
            raise Exception(f"Failed to fetch {url}, status code: {response.status_code}")

    # Function to handle downloading and processing of URLs
    def mapURLs(urlList):
        results = {}
        with ThreadPoolExecutor() as exec:
            futures = []
            # Submit tasks for concurrent download
            for i in range(len(urlList)):
                future = exec.submit(getUrl, urlList[i])
                futures.append((future, urlList[i]))  # Keep track of the future and its associated URL

            # Collect results from futures
            for future, url in futures:
                try:
                    data = future.result()
                    results[url] = data
                except Exception as e:
                    print(f"Error downloading {url}: {e}")
        return results

    # Function to generate URL list based on input
    def getUrlList(number):
        urlList = ["https://www.sample-videos.com/img/Sample-jpg-image-50kb.jpg" for i in range(number)]
        return urlList

    # Function to process and sum results
    def process(n):
        url_list = getUrlList(n)
        results = mapURLs(url_list)
        total = sum(results.values())  # Sum up all values from the results dictionary
        return results, total

    results, total = process(n)
    print(f"Downloaded data from {n} URLs. Results: {results}")
    print(f"Total sum of downloaded data: {total}")

solve(20)
