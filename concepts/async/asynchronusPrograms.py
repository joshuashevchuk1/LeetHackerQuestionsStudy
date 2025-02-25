import asyncio

async def sleep():
    await asyncio.sleep(5)

async def hello():
    print("hello_world")

async def main():
    await sleep() # wait for a responses
    await hello() # allow response regardless

asyncio.run(main())