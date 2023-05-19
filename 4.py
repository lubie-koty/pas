import asyncio
from websockets.server import serve


async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)


async def run_server():
    async with serve(echo, '127.0.0.1', 135):
        await asyncio.Future()


asyncio.run(run_server())
