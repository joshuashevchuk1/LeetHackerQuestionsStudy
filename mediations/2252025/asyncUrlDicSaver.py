import asyncio
import aiohttp

async def get_url_example(url,session):
    async with session.get(url) as response:
        return await response.json()


async def main():
    # urls = ["https://jsonplaceholder.typicode.com/posts" for i in range(50000)]
    url = "https://jsonplaceholder.typicode.com/todos/"
    urls = [url+str(i) for i in range(1,200)] # max is 200
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_url_example(url,session)) for url in urls]
        url_map = {}

        responses = await asyncio.gather(*tasks)
        for url,response in zip(urls,responses):
            url_map[url] = response

        for key,value in url_map.items():
            print('key : ', key, 'value : ', value)

if __name__ == "__main__":
    asyncio.run(main())