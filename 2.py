import asyncio
from websockets.sync.client import connect


async def ws():
    async with connect('ws://echo.websocket.org:80') as websocket:
        user_input = input('msg: ').encode('utf-8')
        await websocket.send(user_input[:125].decode('utf-8'))
        response = await websocket.recv()
        print(response)


asyncio.get_event_loop().run_until_complete(ws())
