import asyncio
import time

async def sleep(n):
    print('before ',n)
    await asyncio.sleep(1)
    print('after ', n)

async def hello():
    print("hello_world")

async def main():
    start = time.time()
    task = asyncio.create_task(sleep(2))
    await sleep(1) # wait for a responses
    await task
    await hello() # allow response regardless
    print("diff: ", time.time()-start)

asyncio.run(main())