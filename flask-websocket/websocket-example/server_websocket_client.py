import asyncio
import websockets


async def connect():
    while True:
        async with websockets.connect("ws://wskkari.gabia.io") as websocket:
            name = input("What's your name? ")
            if name == '-1':
                return

            await websocket.send(name)
            print(f"> {name}")

            greeting = await websocket.recv()
            print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(connect())
