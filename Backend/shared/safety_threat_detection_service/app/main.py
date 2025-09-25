from fastapi import FastAPI

app = FastAPI(title='Safety & Threat Detection')

@app.get('/health')
async def health():
    return {"service": "safety", "status": "ok"}

@app.post('/panic')
async def panic_alert(payload: dict):
    return {"alert_received": True, "payload": payload}
