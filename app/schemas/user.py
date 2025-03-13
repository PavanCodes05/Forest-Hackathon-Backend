from pydantic import BaseModel, EmailStr, PositiveInt
from typing import Optional


class Signup(BaseModel):
    name: str
    email: EmailStr
    password: str
    contact: str
    designation: str
    district: str

class Login(BaseModel):
    email: str
    password: str

class UserProfile(BaseModel):
    name: str
    email: EmailStr
    password: str
    contact: str
    designation: str
    district: str
    cases_involved: Optional[PositiveInt] = 0
    cases_resolved: Optional[PositiveInt] = 0