from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import authRoute, deviceRoute

app = FastAPI( 
    title="AI-driven Illegal Logging & Poaching Detection System" 
) 

app.add_middleware(
     CORSMiddleware, 
     allow_origins=["*"], 
     allow_credentials=True, 
     allow_methods=["*"], 
     allow_headers=["*"], 
)

app.include_router(authRoute.router, prefix="/api/auth", tags=["authentication"])
app.include_router(deviceRoute.router, prefix="/api/devices", tags=["devices"])

@app.get("/", tags=["root"])
async def root():
    return {"message": "Welcome to the application"}