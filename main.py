from fastapi import FastAPI, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from models.auth_models import EmpsModel, UserRegistration, EmpRegistration
from routes.auth_routes import router as auth_router
from auth.jwt_handler import decodeJWT, signJWT
from models.auth_models import AuthModel
from settings import get_db
from routes.employee_routes import router as employee_router


from models.auth_models import EmpsModel, UserRegistration, EmpRegistration



app = FastAPI()
from settings import get_db

# Include the authentication router
app.include_router(auth_router, prefix="/auth", tags=["auth"])

class UserLoginJSON(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None

MIN_TOKEN_LENGTH = 8


app.include_router(employee_router, tags=["employee"])

app.include_router(auth_router, prefix="/auth", tags=["auth"])

app.include_router(employee_router, tags=["employee"])

app.include_router(employee_router, tags=["employee"])


