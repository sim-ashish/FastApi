from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import HTMLResponse
from typing import List
import json

app = FastAPI()

# In-memory list of connected WebSocket clients
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            await connection.send_json(message)

manager = ConnectionManager()

@app.get("/")
async def get():
    html = """
    <!DOCTYPE html>
    <html>
        <head><title>Webhook Listener</title></head>
        <body>
            <h1>Webhook Listener (WebSocket)</h1>
            <ul id='messages'></ul>
            <script>
                const ws = new WebSocket("ws://localhost:8000/ws");
                ws.onmessage = function(event) {
                    const messages = document.getElementById('messages');
                    const message = document.createElement('li');
                    message.textContent = event.data;
                    messages.appendChild(message);
                };
            </script>
        </body>
    </html>
    """
    return HTMLResponse(html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()  # Not used, but keeps connection alive
    except WebSocketDisconnect:
        manager.disconnect(websocket)

@app.post("/send-webhook")
async def send_webhook(request: Request):
    body = await request.json()
    await manager.broadcast(body)
    return {"status": "Webhook delivered to WebSocket clients"}
