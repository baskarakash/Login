# employee_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.auth_models import EmpsModel, EmpRegistration
from settings import get_db

router = APIRouter()

@router.post("/register_employee")
async def register_employee(user1: EmpRegistration, db: Session = Depends(get_db)):
    existing_employee = db.query(EmpsModel).filter(EmpsModel.empid == user1.employeeid).first()

    if existing_employee:
        raise HTTPException(status_code=400, detail="Employee already registered")

    new_employee = EmpsModel(
        empname=user1.employeename,
        empid=user1.employeeid,  # Keep it as a string
        empage=user1.employeeage,
        empsalary=user1.employeesalary
    )

    db.add(new_employee)
    db.commit()

    return {"message": "Employee registration successful"}
