from fastapi import FastAPI

app = FastAPI(title='Analytics')

@app.get('/health')
async def health():
    return {"service": "analytics", "status": "ok"}

@app.get('/eta')
async def eta_stub():
    return {"eta_minutes": 5}
