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
    try:
        await asyncio.gather(asyncio.wait_for(sleep(1),5), sleep(2), hello()) # runs all these methods in parrell
    except asyncio.TimeoutError as e:
        print("got an exception : ",e)
    print("diff: ", time.time()-start)

asyncio.run(main())