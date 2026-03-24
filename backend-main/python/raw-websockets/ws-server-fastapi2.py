"""
You will need to install (at least) fastapi and websockets
pip install fastapi websockets

then to be compatible with the client, run this with
fastapi run ws-server-fastapi2.py --port 8765
"""

import asyncio

from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/")
async def coutdown_endpoint(websocket: WebSocket):
    """
    a little more advanced ws server
    it receives an integer, and then sends back that amount of messages to the client
    (aka the countdown protocol)
    """
    await websocket.accept()
    while True:
        message = await websocket.receive_text()
        print("Received: ", message)
        try:
            count = int(message)
        except ValueError:
            await websocket.send_text("Please send an integer")
            continue
        while count > 0:
            await websocket.send_text(str(count := count-1))
            await asyncio.sleep(1)
