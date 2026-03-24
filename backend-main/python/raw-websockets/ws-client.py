"""
This is a simple WebSocket client that sends a message to the server, receives a response and exits
"""

import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello, WebSocket! from Python")
        response = await websocket.recv()
        print(f"Received: {response}")

asyncio.run(hello())
