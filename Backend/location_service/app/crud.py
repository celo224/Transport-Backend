from .models import Location

def create_location(payload):
    return {"ingested": True, "payload": payload.dict()}
