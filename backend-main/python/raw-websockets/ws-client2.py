import asyncio
import websockets
import argparse

# pass the count as an argument
parser = argparse.ArgumentParser(description="Send a message to the server and receive a response")
parser.add_argument("count", type=int)
args = parser.parse_args()
count = args.count

async def hello():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send(str(count))
        while True:
            response = await websocket.recv()
            print(f"Received: {response}")
            if response == "0":
                print("Countdown finished")
                break

asyncio.run(hello())
