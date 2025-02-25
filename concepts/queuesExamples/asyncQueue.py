import asyncio
import random

async def producer(queue, producer_id, num_items):
    """Produces items and places them in the queue."""
    for i in range(num_items):
        item = f"P{producer_id}-Item{i}"
        await queue.put(item)  # Blocks if full
        print(f"Producer {producer_id} -> {item}")
        await asyncio.sleep(random.uniform(0.1, 0.5))  # Simulate work

async def consumer(queue, consumer_id):
    """Consumes items from the queue and exits when queue is empty & producers are done."""
    while True:
        item = await queue.get()  # Blocks if empty
        if item is None:  # Sentinel value signals termination
            break
        print(f"Consumer {consumer_id} <- {item}")
        await asyncio.sleep(random.uniform(0.2, 0.7))  # Simulate processing
        queue.task_done()  # Mark item as processed

async def main(n_producers=4, m_consumers=3, num_items_per_producer=5):
    queue = asyncio.Queue(maxsize=5)  # Bounded queue

    # Create producer and consumer tasks
    producers = [asyncio.create_task(producer(queue, i, num_items_per_producer)) for i in range(n_producers)]
    consumers = [asyncio.create_task(consumer(queue, i)) for i in range(m_consumers)]

    # Wait for all producers to finish
    await asyncio.gather(*producers)

    # Signal consumers to exit by adding None to queue (one for each consumer)
    for _ in range(m_consumers):
        await queue.put(None)

    # Wait for consumers to finish
    await asyncio.gather(*consumers)

# Run the async event loop
asyncio.run(main(n_producers=4, m_consumers=3, num_items_per_producer=5))
