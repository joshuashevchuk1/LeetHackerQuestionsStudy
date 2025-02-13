import aiohttp
import asyncio

async def fetch(url, session):
    async with session.get(url) as response:
        return await response.read() if response.status == 200 else None

async def concurrentUrlDownload(urls):
    result = {}
    async with aiohttp.ClientSession() as session:
        tasks = {url: fetch(url, session) for url in urls}
        results = await asyncio.gather(*tasks.values())

        for url, content in zip(tasks.keys(), results):
            if content:
                result[url] = content
    return result
