import requests
from bs4 import BeautifulSoup


# kinda useless here
class WikiWorker():
    def __init__(self):
        self._url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

    def _extract_company_symbols(self, page_html):
        soup = BeautifulSoup(page_html)
        table = soup.find(id = "constituents")
        table_rows = table.find_all('tr')
        for table_row in table_rows:
            symbol = table_row.find('td').text.strip('\n')
            yield symbol

    def get_s_p_500_companies(self):
        responses = requests.get(url=self._url)
        if responses.status_code != 200:
            return []
        yield from self._extract_company_symbols(page_html=responses.text)

wikiWorker = WikiWorker()
for symbol in wikiWorker.get_s_p_500_companies():
    print(symbol)