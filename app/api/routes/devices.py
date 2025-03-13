from fastapi import APIRouter, status, HTTPException
from app.schemas.device import Device

router = APIRouter()

@router.post("/", response_model=Device, status_code=status.HTTP_200_OK)
async def fn(Device: Device):
    return {"Hello": "It is working"}