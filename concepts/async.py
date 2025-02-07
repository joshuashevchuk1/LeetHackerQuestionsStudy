import asyncio

from sqlalchemy.testing import future


async def helloWorld():
    print("helloworld")

async def helloWorldN(n):
    tasks = [helloWorld() for i in range(n)]
    await asyncio.gather(*tasks)


asyncio.run(helloWorldN(5))

from concurrent.futures import ThreadPoolExecutor

from concurrent.futures import ThreadPoolExecutor, as_completed


def batchExample():
    def action(i):
        print(f"Task {i}: helloWorld")

    def getActions(n):
        return [lambda i=i: action(i) for i in range(n)]  # Store function references

    def cycle(actions, batch_size):
        with ThreadPoolExecutor() as executor:
            for i in range(0, len(actions), batch_size):
                batch = actions[i:i + batch_size]  # Take `batch_size` actions at a time
                futures = [executor.submit(a) for a in batch]

                # Wait for the batch to finish before moving to the next
                for future in as_completed(futures):
                    future.result()  # Ensures exceptions are raised if any

    def process(n, k):
        actions = getActions(n)  # Generate all actions once
        cycle(actions, k)  # Process in batches of `k`

    n = 5000  # Total tasks
    k = 5  # Batch size

    process(n, k)

batchExample()