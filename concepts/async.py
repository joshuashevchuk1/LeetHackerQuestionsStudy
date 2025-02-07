import asyncio

async def helloWorld():
    print("helloworld")

async def helloWorldN(n):
    tasks = [helloWorld() for i in range(n)]
    await asyncio.gather(*tasks)


asyncio.run(helloWorldN(5))