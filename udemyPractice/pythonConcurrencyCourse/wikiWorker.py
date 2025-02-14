from http.client import responses

import requests
from bs4 import BeautifulSoup


# kinda useless here
class WikiWorker():
    def __init__(self):
        self._url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

    def _extract_company_symbols(self):
        return

    def get_s_p_500_companies(self):
        responses = requests.get(url=self._url)
        if responses.status_code != 200:
            return []