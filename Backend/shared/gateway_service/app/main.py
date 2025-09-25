from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware
import httpx

app = FastAPI(title='TransitFlow Gateway')
router = APIRouter()

@app.get('/')
async def root():
    return {"service": "gateway", "status": "ok"}

@router.get('/location/health')
async def location_health():
    async with httpx.AsyncClient() as client:
        r = await client.get('http://location_service:8000/health')
        return r.json()

app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)
