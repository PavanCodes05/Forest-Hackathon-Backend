from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import authentication

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

app.include_router(authentication.router, prefix="/api/auth", tags=["authentication"])

@app.get("/", tags=["root"])
async def root():
    return {"message": "Welcome to the application"}