import asyncio
import time

import aiohttp

from collections import defaultdict

from queue import Queue

async def getUrl(session, url):
        async with session.get(url) as response:
            return await response.json()

async def main():
    url = "https://jsonplaceholder.typicode.com/todos/"
    urls = [url+str(i) for i in range(1,1000)]
    url_map = defaultdict(list)

    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [getUrl(session, url) for url in urls]
        responses = await asyncio.gather(*tasks, return_exceptions=True)

    for url, content in zip(urls, responses):
            if content:
               url_map[url] = content

    end = time.time()

    for key,value in url_map.items():
        print('key : ', key ,' value : ', value)

    print('clock : ', end - start)

if __name__ == "__main__":
    asyncio.run(main())