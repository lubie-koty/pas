import asyncio
from websockets.sync.client import connect


async def ws():
    async with connect('ws://echo.websocket.org:80') as websocket:
        await websocket.send('Hello world!')
        response = await websocket.recv()
        print(response)


asyncio.get_event_loop().run_until_complete(ws())
