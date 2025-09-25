from fastapi import FastAPI, WebSocket

app = FastAPI(title='Real-time API')

@app.get('/health')
async def health():
    return {"service": "real_time", "status": "ok"}

@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"echo: {data}")
