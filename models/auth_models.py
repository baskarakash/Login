# models/auth_models.py
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class AuthModel(Base):
    __tablename__ = "auth"
    userid = Column(String(256), primary_key=True)
    pas = Column(String(256))

class UserRegistration(BaseModel):
    username: str
    password: str
    repeat_password: str

class EmpsModel(Base):
    __tablename__ = "employee"

    empid = Column(String, primary_key=True, index=True)
    empname = Column(String, index=True)
    empage = Column(String)  # Updated to character varying
    empsalaray = Column(String) # Corrected the column name

class EmpRegistration(BaseModel):
    employeename: str
    employeeid: str
    employeeage: str
    employeesalary: str
