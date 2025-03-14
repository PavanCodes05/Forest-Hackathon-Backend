from fastapi import APIRouter, status, HTTPException
from app.schemas.device import Device
from app.firebase_client import db, messaging
from datetime import datetime

router = APIRouter()
device_collection = db.child("devices")

@router.post("/add", response_model=Device, status_code=status.HTTP_201_CREATED)
async def add_device(device: Device):
    try:
        # Push new data to Firebase (generates a unique key)
        if not device.installation_date:
            device.installation_date = datetime.today().strftime("%Y-%m-%d")
        new_device_ref = device_collection.push(device.model_dump(exclude={"id"}))
        device.id = new_device_ref.key  # Firebase returns the generated key

        message = messaging.Message(
            notification=messaging.Notification(
                title="New Device Added",
                body="Notification Body Test"
            ),
            data={"type": "Gunshot", "confidence": "100%"},
            topic="all"
        )
        messaging.send(message)

        return device
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error adding device: {str(e)}")

    
@router.get("/", response_model=list[Device], status_code=status.HTTP_200_OK)
async def get_devices():
    try:
        devices_data = device_collection.get()

        if not devices_data:
            return []

        # Convert Firebase data into a list of Device objects
        devices = [Device(id=key, **value) for key, value in devices_data.items()]
        
        return devices
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error fetching devices: {str(e)}")
