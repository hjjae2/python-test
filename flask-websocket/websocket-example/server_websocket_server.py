import asyncio
import datetime
import random
import websockets
import json
import logging


logging.basicConfig()

STATE = {"value": 0}

USERS = set()

async def serve(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    gretting = f"Hello {name}!"
    await websocket.send(gretting)
    print(f"> {gretting}")


async def time(websocket, path):
    while True:
        name = "Hello, World!"
        now = datetime.datetime.now().isoformat()
        await websocket.send(now + " : " + name)
        await asyncio.sleep(random.random() * 3)


def state_event():
    return json.dumps({"type": "state", **STATE})


def users_event():
    return json.dumps({"type": "users", "count": len(USERS)})


async def notify_state():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = state_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def notify_users():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = users_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def register(websocket):
    USERS.add(websocket)
    await notify_users()


async def unregister(websocket):
    USERS.remove(websocket)
    await notify_users()


async def counter(websocket, path):
    # register(websocket) sends user_event() to websocket
    await register(websocket)
    try:
        await websocket.send(state_event())
        async for message in websocket:
            data = json.loads(message)
            if data["action"] == "minus":
                STATE["value"] -= 1
                await notify_state()
            elif data["action"] == "plus":
                STATE["value"] += 1
                await notify_state()
            else:
                logging.error("unsupported event: %s", data)
    finally:
        await unregister(websocket)

# start_server = websockets.serve(serve, "localhost", 3000)
# start_server = websockets.serve(time, "localhost", 3000)
start_server = websockets.serve(counter, "localhost", 3000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
