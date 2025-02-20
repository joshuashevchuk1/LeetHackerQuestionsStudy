import threading
import requests

class Requestor(threading.Thread):
    def __init__(self, url , file_name,**kwargs):
        super(Requestor, self).__init__(**kwargs)
        self._url = url
        self.file_name = file_name
        self.response = None
        self.start()

    def getRequest(self):
        self.response = requests.get(self._url)

    def writeResponse(self):
        if self.response.status_code == 200:
            with open(str(self.file_name),'wb') as f:
                f.write(self.response.content)

    def run(self):
        self.getRequest()
        self.writeResponse()

def getUrlList(number):
    urlList = ["https://www.sample-videos.com/img/Sample-jpg-image-50kb.jpg" for i in range(number)]
    return urlList

n = 5
urlList = getUrlList(n)
print(urlList)

threads = []

for i in range(len(urlList)):
    threads.append(Requestor(urlList[i], str(i) + ".jpg"))

for thread in threads:
    thread.join()