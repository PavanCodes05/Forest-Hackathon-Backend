from fastapi import APIRouter, status, HTTPException ,Depends
from firebase_admin import auth,db
from app.schemas.user import Signup, Login, UserProfile


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





@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: Signup):
    try:
        
        user_record = auth.create_user(
            email=user.email,
            password=user.password,
            display_name=user.name
        )
        
        user_profile = UserProfile(**user.dict())
        db.collection("users").document(user_record.uid).set(user_profile.dict())
        return {"message": "User registered successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
async def login(credentials: Login):
    try:
       
        user = auth.sign_in_with_email_and_password(credentials.email, credentials.password)
        return {"message": "Login successful", "token": user['idToken']}
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid email or password")