### Example #1: Concurrent File Download

# Implement a function that, given an array of URLs and an existing download function, downloads all the data from the urls in parallel,
# merges the results into a single dictionary of {url:data} and then returns the dictionary.
#
# Result: they are separate JSON payloads w/o overlapping keys. i.e.,
# the download result of each URL is a number and we want to return the total sum at the end.


import asyncio
import requests
import aiohttp

def solution():
    async def getURL(url,filePath):
        response = requests.get(url)
        if response.status_code == 200:
            with open(str(filePath),'wb') as f:
                f.write(response.content)
        else:
            raise Exception("did not get 200 : ", response.status_code)

    async def mapURLS(urlList):
        tasks = []
        for i in range(len(urlList)):
            tasks.append(getURL(urlList[i], str(i) + ".jpg"))
        await asyncio.gather(*tasks)

    def getUrlList(number):
        urlList = ["https://www.sample-videos.com/img/Sample-jpg-image-50kb.jpg" for i in range(number)]
        return urlList

    def solve():
        number = 20
        urlList = getUrlList(number)
        asyncio.run(mapURLS(urlList))

    solve()

#solution()

# even better solution

from concurrent.futures import ThreadPoolExecutor

def evenBetter(n):
    def getURL(url, filePath):
        response = requests.get(url)
        if response.status_code == 200:
            with open(str(filePath), 'wb') as f:
                f.write(response.content)
        else:
            raise Exception(f"Failed to download {url}, status code: {response.status_code}")

    def mapURLS(urlList):
        with ThreadPoolExecutor() as executor:
            for i in range(len(urlList)):
                # Submit each download task to the thread pool
                executor.submit(getURL, urlList[i], str(i) + ".jpg")

    def getUrlList(number):
        urlList = ["https://www.sample-videos.com/img/Sample-jpg-image-50kb.jpg" for _ in range(number)]
        return urlList

    def solve(n):
        urlList = getUrlList(n)
        mapURLS(urlList)

    solve(n)

evenBetter(40)

# better solution

def better():

    async def getURL(url, filePath):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    with open(str(filePath), 'wb') as f:
                        f.write(await response.read())
                else:
                    raise Exception(f"Failed to get {url}, status code: {response.status}")

    async def mapURLS(urlList):
        tasks = []
        for i in range(len(urlList)):
            tasks.append(getURL(urlList[i], str(i) + ".jpg"))
        await asyncio.gather(*tasks)

    def getUrlList(number):
        urlList = ["https://www.sample-videos.com/img/Sample-jpg-image-50kb.jpg" for i in range(number)]
        return urlList

    number = 5
    urlList = getUrlList(number)

    asyncio.run(mapURLS(urlList))

#better()
