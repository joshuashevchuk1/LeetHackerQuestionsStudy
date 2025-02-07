import requests

def getHttpBin():
    url = "https://httpbin.org/get"
    response = requests.get(url)
    json = response.json()
    print(json)

getHttpBin()


def download_file(url, destination):
    # Send GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        with open(destination, 'wb') as f:  # Open file in write-binary mode
            f.write(response.content)  # Write the content to the file
        print(f"File downloaded successfully and saved as {destination}")
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")

file_url = "https://www.sample-videos.com/img/Sample-jpg-image-50kb.jpg"
destination_path = "downloaded_sample.pdf"
download_file(file_url, destination_path)