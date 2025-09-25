from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine
import os

app = FastAPI(title='User Reports Service')

@app.on_event('startup')
async def on_startup():
    db_url = f"postgresql://{os.getenv('POSTGRES_USER','transit')}:{os.getenv('POSTGRES_PASSWORD','transit')}@{os.getenv('POSTGRES_HOST','postgres')}:{os.getenv('POSTGRES_PORT',5432)}/{os.getenv('POSTGRES_DB','transitdb')}"
    engine = create_engine(db_url)
    SQLModel.metadata.create_all(engine)

@app.get('/health')
async def health():
    return {"service": "user_reports", "status": "ok"}

@app.post('/reports')
async def create_report(report: dict):
    return {"saved": True, "report": report}
