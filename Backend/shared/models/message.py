from pydantic import BaseModel
from typing import Any, Dict

class KafkaMessage(BaseModel):
    topic: str
    payload: Dict[str, Any]
