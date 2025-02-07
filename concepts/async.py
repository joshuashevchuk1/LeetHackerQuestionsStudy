import asyncio

from torch.onnx.symbolic_opset11 import gather


async def helloWorld():
    print("helloworld")

async def helloWorldN(n):
    tasks = [helloWorld() for i in range(n)]
    await gather(tasks)


helloWorldN(5)