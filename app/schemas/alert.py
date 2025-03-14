from pydantic import BaseModel
from typing import Optional
from datetime import datetime
class CreateAlert(BaseModel):
    device_id: str
    type: str
    confidence_score: float
    status: str = "new"

class SendAlert(CreateAlert):
    coordinates: str
    timestamp: datetime