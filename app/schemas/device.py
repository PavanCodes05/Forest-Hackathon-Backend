from pydantic import BaseModel
from typing import Optional
from datetime import date

class Device(BaseModel):
    id: Optional[str] = None
    name: str
    coordinates: str 
    installation_date: Optional[str] = None