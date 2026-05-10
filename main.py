from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from typing import List

app = FastAPI()

clients: List[WebSocket] = []

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def get():
    return FileResponse("index.html")

async def broadcast(message: str):
    for client in clients:
        try:
            await client.send_text(message)
        except:
            clients.remove(client)

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await websocket.accept()
    clients.append(websocket)
    try:
        await broadcast(f"{username} joined the chat")
        while True:
            data = await websocket.receive_text()
            await broadcast(f"{username}: {data}")
    except WebSocketDisconnect:
        clients.remove(websocket)
        await broadcast(f"{username} left the chat")