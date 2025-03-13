from fastapi import APIRouter, status, HTTPException
from firebase_admin import auth

router = APIRouter()

"""
    Sample Code:
    @router.post("/signup", response_model=schema, status_code=status.HTTP_201_CREATED)
    function(params: schema(pydantic model)): {
    try: 
        .....
    except Exception as e:
        raise HTTPException(
        status_code = status.HTTP_400_BAD_REQUEST,
        detail = f"Error Creating User"
    )}
"""