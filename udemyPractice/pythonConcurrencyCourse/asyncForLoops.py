import asyncio
import time

# the goal of the gather method is to allow async calls to start at the same time

async def sleep(n):
    print('before ',n)
    n = max(2,n)
    for i in range(1,n):
        yield i
        await asyncio.sleep(i) # waits until this coroutine is finished
    print('after ', n)

async def hello():
    print("hello_world")

async def main():
    start = time.time()
    async for k in sleep(5):
        print(k)
    print("diff: ", time.time()-start)

asyncio.run(main())