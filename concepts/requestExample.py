import requests

def getGoogle():
    url = "https://www.google.com"
    requests.get(url)
    response = requests.Response
    body = response.text
    print(body)

getGoogle()
