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
        empid=user1.employeeid,  
        empage=user1.employeeage,
        empsalary=user1.employeesalary
    )

    db.add(new_employee)
    db.commit()

    return {"message": "Employee registration successful"}

@router.get("/get_employee/{employee_id}", response_model=dict)
async def get_employee(employee_id: str, db: Session = Depends(get_db)):
    employee = db.query(EmpsModel).filter(EmpsModel.empid == employee_id).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {
        "empid": employee.empid,
        "empname": employee.empname,
        "empage": employee.empage,
        "empsalaray": employee.empsalaray
    }



@router.delete("/delete_employee/{employee_id}", tags=["employee"])
async def delete_employee(employee_id: str, db: Session = Depends(get_db)):
    existing_employee = db.query(EmpsModel).filter(EmpsModel.empid == employee_id).first()

    if not existing_employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(existing_employee)
    db.commit()

    return {"message": "Employee deleted successfully"}


@router.put("/update_employee/{employee_id}", tags=["employee"])
async def update_employee(employee_id: str, updated_data: EmpRegistration, db: Session = Depends(get_db)):
    existing_employee = db.query(EmpsModel).filter(EmpsModel.empid == employee_id).first()

    if not existing_employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    # Update the employee data
    existing_employee.empname = updated_data.employeename
    existing_employee.empage = updated_data.employeeage
    existing_employee.empsalary = updated_data.employeesalary

    db.commit()

    return {"message": "Employee updated successfully"}
