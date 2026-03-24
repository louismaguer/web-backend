"""
a little more advanced ws server
it receives an integer, and then sends back that amount of messages to the client
(aka the countdown protocol)
"""

import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        print("Received: ", message)
        try:
            count = int(message)
        except ValueError:
            await websocket.send("Please send an integer")
            continue
        while count > 0:
            await websocket.send(str(count := count-1))
            await asyncio.sleep(1)

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # Run forever

asyncio.run(main())
