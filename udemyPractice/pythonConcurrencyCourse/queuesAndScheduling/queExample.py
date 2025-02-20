import threading
from queue import Queue
import requests

class RequestWorker(threading.Thread):
    mutex = threading.Lock()

    def __init__(self, queue):
        super(RequestWorker, self).__init__()
        self._queue = queue
        self.session = requests.Session()
        self.start()

    def getRequest(self, url):
        response = self.session.get(url)
        return response

    def writeResponse(self, response, file_name):
        if response and response.status_code == 200:
            print("Writing:", file_name)
            with open(file_name, 'wb') as f:
                f.write(response.content)

    def run(self):
        while True:
            url, file_name = self._queue.get()
            if url is None:
                self._queue.task_done()
                break
            response = self.getRequest(url)
            self.writeResponse(response, file_name)
            self._queue.task_done()

def getUrlList(number):
    return ["https://www.sample-videos.com/img/Sample-jpg-image-50kb.jpg" for _ in range(number)]

n = 5
urlList = getUrlList(n)

queue = Queue()

num_threads = 3  # Number of worker threads
for _ in range(num_threads):
    worker = RequestWorker(queue)

for i in range(len(urlList)):
    queue.put((urlList[i], f"{i}.jpg"))

queue.join()
for _ in range(num_threads):
    queue.put((None, None))
