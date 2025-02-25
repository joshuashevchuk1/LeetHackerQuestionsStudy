import asyncio
import time

import aiohttp
import requests

async def get_url_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    start_time = time.time()
    urls = ["https://www.google.com/" for i in range (5)]
    print(urls)

    sync_test_response = []
    for url in urls:
        sync_test_response.append(requests.get(url).text)

    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(get_url_response(url)))

    async_text_response = await asyncio.gather(*tasks) # * is argument unpacking
    print(async_text_response)
    print("diff : ", time.time() - start_time)

if __name__ == "__main__":
    asyncio.run(main())