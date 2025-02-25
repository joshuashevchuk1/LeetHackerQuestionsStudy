import asyncio

async def producer(queue):
    print("Producing")
    await queue.put(1)

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f"Consuming {item}")
        queue.task_done()  # Mark task as completed

async def main():
    queue = asyncio.Queue()

    tasks = []

    for i in range(5):
        tasks.append(asyncio.create_task(producer(queue)))

    for i in range(5):
        tasks.append(asyncio.create_task(consumer(queue)))

    response = await asyncio.gather(*tasks)
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
