from concurrent.futures.thread import ThreadPoolExecutor

import requests


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

solve(20)