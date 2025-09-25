from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import BaseModel

class Location(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    device_id: str
    lat: float
    lon: float
    ts: int

class LocationCreate(BaseModel):
    device_id: str
    lat: float
    lon: float
    ts: int
