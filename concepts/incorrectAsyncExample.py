
import asyncio

async def printAsync():
    for i in range(5):
        print("hello")

async def chronus():
    await printAsync()


async def main():
    tasks = []
    for i in range(5):
        tasks.append(asyncio.create_task(chronus()))

    await asyncio.gather(*tasks)


if __name__  == "__main__":
    asyncio.run(main())