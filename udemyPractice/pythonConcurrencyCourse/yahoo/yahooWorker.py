import threading

class YahooWorker(threading.Thread):
    def __init__(self,symbol, **kwargs):
        super(YahooWorker,self).__init__(**kwargs)
        self._symbol = symbol
        base_url = "https://finance.yahoo.com/quote/"
        url = f'{base_url},{self._symbol}'
        self.start()

    def run(self):
        pass