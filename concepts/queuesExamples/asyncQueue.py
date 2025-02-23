import asyncio
import random

async def producer(queue, producer_id):
    """Produces items and places them in the queue."""
    for i in range(5):  # Each producer produces 5 items
        item = f"P{producer_id}-Item{i}"
        await queue.put(item)  # Blocks if full
        print(f"Producer {producer_id} -> {item}")
        await asyncio.sleep(random.uniform(0.1, 0.5))  # Simulate work

async def consumer(queue, consumer_id):
    """Consumes items from the queue."""
    while True:
        item = await queue.get()  # Blocks if empty
        print(f"Consumer {consumer_id} <- {item}")
        queue.task_done()  # Mark task as done
        await asyncio.sleep(random.uniform(0.2, 0.7))  # Simulate processing time

async def main(n_producers=3, m_consumers=2):
    queue = asyncio.Queue(maxsize=5)  # Bounded queue

    # Create producer and consumer tasks
    producers = [asyncio.create_task(producer(queue, i)) for i in range(n_producers)]
    consumers = [asyncio.create_task(consumer(queue, i)) for i in range(m_consumers)]

    await asyncio.gather(*producers)  # Wait for all producers to finish

    # Once all producers are done, allow consumers to exit gracefully
    for _ in range(m_consumers):
        await queue.put(None)  # Sentinel value for consumers to exit

    await asyncio.gather(*consumers, return_exceptions=True)  # Let consumers exit

# Run the async event loop
asyncio.run(main(n_producers=4, m_consumers=3))
