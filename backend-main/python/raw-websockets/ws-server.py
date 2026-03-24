"""
a simple ws server: implements the ping pong protocol
(aka "what you get is teg uoy tahw")
"""

import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        print("Received: ", message)
        # reverse the message
        await websocket.send(message[::-1])

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # Run forever

asyncio.run(main())
