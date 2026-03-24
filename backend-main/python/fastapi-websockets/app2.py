from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import datetime

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, data: dict):
        # Broadcast the dictionary as a JSON object
        for connection in self.active_connections:
            await connection.send_json(data)

manager = ConnectionManager()

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket)
    try:
        while True:
            # Receive JSON from a client
            data = await websocket.receive_json()

            # Enrich the data with server-side info (timestamp)
            payload = {
                "status": data["status"],
                "sender": client_id,
                "time": datetime.datetime.now().strftime("%H:%M:%S")
            }

            await manager.broadcast(payload)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
