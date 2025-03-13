from pydantic import BaseModel
from datetime import date

class Device(BaseModel):
    id: str
    coordinates: str 
    instalation_date: date