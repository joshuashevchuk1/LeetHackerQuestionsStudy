import asyncio

from sqlalchemy.util import await_only


async def sleep(i):
    await asyncio.sleep(2)
    return i

async def main():
    pending = set()
    for i in range(1,11):
        pending.add(asyncio.create_task(sleep(i)))

    add_task = True

    while len(pending) > 0:
        done, pending = await asyncio.wait(pending,return_when="FIRST_COMPLETED")
        for task in done:
            print(await task)
        if add_task:
            pending.add(asyncio.create_task(sleep(1)))
            add_task = False



if __name__ == "__main__":
    asyncio.run(main())