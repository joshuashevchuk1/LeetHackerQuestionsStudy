import asyncio

async def producer(queue):
    await queue.put(1)
    return "produced 1"

async def consumer(queue):
    item = await queue.get()
    print(f"Consuming {item}")
    queue.task_done()
    return item

async def main():
    queue = asyncio.Queue()

    tasks = []

    n = 5

    for i in range(n):
        tasks.append(asyncio.create_task(producer(queue)))
        tasks.append(asyncio.create_task(consumer(queue)))

    response = await asyncio.gather(*tasks)
    print(response)

if __name__ == "__main__":
    asyncio.run(main())