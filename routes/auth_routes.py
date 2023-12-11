 #routers/auth_routes.py
from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from models.auth_models import AuthModel, UserRegistration
from auth.jwt_handler import signJWT, decodeJWT
from pydantic import BaseModel
from typing import Optional
from starlette.responses import JSONResponse
from settings import MIN_TOKEN_LENGTH, get_db, oauth2_scheme

router = APIRouter()

class UserLoginJSON(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None

async def get_current_user(token: str = Depends(decodeJWT)):
    if not token:
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

@router.post("/submitted", tags=["user"], response_model=dict)
async def login_user(
    user_data: UserLoginJSON = None,
    authorization: str = Header(...),  # Require the Authorization header
    db: Session = Depends(get_db),
):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format in Authorization header")

    token_value = authorization[len("Bearer "):].strip()

    if len(token_value) < MIN_TOKEN_LENGTH:
        raise HTTPException(status_code=401, detail="Invalid token length")

    try:
        current_user = get_current_user(token_value)
        return {"message": "Successful Login!!!"}
    except HTTPException as e:
        if e.status_code == 401:
            raise HTTPException(status_code=401, detail="No access to login")
        else:
            raise e

@router.post("/register", tags=["user"], response_model=dict)
async def register_user(
    user_data: UserRegistration,
    db: Session = Depends(get_db)
):
    existing_user = db.query(AuthModel).filter(AuthModel.userid == user_data.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    if user_data.password != user_data.repeat_password:
        raise HTTPException(status_code=400, detail="Password and Repeat password do not match")

    new_user = AuthModel(userid=user_data.username, pas=user_data.password)
    db.add(new_user)
    db.commit()

    access_token = signJWT(new_user.userid)

    return {"message": "Registration successful", "access_token": access_token}

# Add other routes and logic as needed
# Example:
# @router.get("/profile", tags=["user"], response_model=dict)
# async def get_user_profile(current_user: str = Depends(get_current_user)):
#     return {"user_profile": current_user}
