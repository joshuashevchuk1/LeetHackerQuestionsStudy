import asyncio


async def main():
    urls = ["https://www.google.com/" for i in range (5)]
    print(urls)

if __name__ == "__main__":
    asyncio.run(main())