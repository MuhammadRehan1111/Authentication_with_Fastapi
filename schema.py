from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional

class create_User(BaseModel):
    name:str
    email:str
    password:str


class UserLogin (BaseModel):
    name:str
    password:str


class UserResponse(Basemodel):
    id:str
    name:str
    email:EmailStr
    created_at:datetime


class Token(BaseModel):
    access_token:str
    token_type:str


class AnalysisRequest(BaseModel):
    text:str

class AnalysisResponse(BaseModel):
    id:str
    User_id:str
    orignal_text:text
    result:dict
    created_at:datetime

    
