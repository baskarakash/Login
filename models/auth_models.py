# models/auth_models.py
from sqlalchemy import Column, String,Integer
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from passlib.context import CryptContext
Base = declarative_base()

class AuthModel(Base):
    __tablename__ = "auth"
    userid = Column(String(256))
    pas = Column(String(256))
    user_id =Column(Integer,primary_key=True)
    

class UserRegistration(BaseModel):
    username: str
    password: str
    repeat_password: str
    repeate_password:str

class EmpsModel(Base):
    __tablename__ = "employee"

    empid = Column(Integer, primary_key=True, index=True)
    empname = Column(String, index=True)
    empage = Column(String)  
    empsalaray = Column(String) 

class EmpRegistration(BaseModel):
    employeename: str
    employeeid: int
    employeeage: str
    employeesalary: str


class PasswordHashing:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def hash_password(cls, password: str) -> str:
        return cls.pwd_context.hash(password)

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return cls.pwd_context.verify(plain_password, hashed_password)



  