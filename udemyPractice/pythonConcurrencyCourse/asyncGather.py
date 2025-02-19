import asyncio
import time

# the goal of the gather method is to allow async calls to start at the same time

async def sleep(n):
    print('before ',n)
    await asyncio.sleep(1) # waits until this coroutine is finished
    print('after ', n)

async def hello():
    print("hello_world")

async def main():
    start = time.time()
    await asyncio.gather(sleep(1), sleep(2), hello()) # runs all these methods in parrell
    print("diff: ", time.time()-start)

asyncio.run(main())