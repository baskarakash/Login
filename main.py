from fastapi import FastAPI, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from models.auth_models import EmpsModel, UserRegistration, EmpRegistration
from routes.auth_routes import router as auth_router
from auth.jwt_handler import decodeJWT, signJWT
from models.auth_models import AuthModel
from settings import get_db

app = FastAPI()

# Include the authentication router
app.include_router(auth_router, prefix="/auth", tags=["auth"])

class UserLoginJSON(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None

MIN_TOKEN_LENGTH = 8

async def get_current_user(token: str = Depends(decodeJWT)):
    if not token:
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

@app.post("/auth/submitted", tags=["user"], response_model=dict)
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

@app.post("/auth/register", tags=["user"], response_model=dict)
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

@app.post("/register_employee")
async def register_employee(user1: EmpRegistration, db: Session = Depends(get_db)):
    existing_employee = db.query(EmpsModel).filter(EmpsModel.empid == user1.employeeid).first()

    if existing_employee:
        raise HTTPException(status_code=400, detail="Employee already registered")

    new_employee = EmpsModel(
        empname=user1.employeename,
        empid=user1.employeeid,  # Keep it as a string
        empage=user1.employeeage,
        empsalaray=user1.employeesalary
    )

    db.add(new_employee)
    db.commit()

    return {"message": "Employee registration successful"}
