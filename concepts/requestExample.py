import requests

def getHttpBin():
    url = "https://httpbin.org/get"
    response = requests.get(url)
    json = response.json()
    print(json)

getHttpBin()
