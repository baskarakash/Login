from sqlalchemy import Column, String, Integer
from app.settings import Base
from pydantic import BaseModel
from passlib.context import CryptContext
from typing import ClassVar


class AuthModel(Base):
    __tablename__ = "auth"
    userid: str = Column(String(256))
    pas: str = Column(String(256))
    user_id: int = Column(Integer, primary_key=True)

# class UserRegistration(Base):
#     __tablename__ = ""
#     username: str
#     password: str
#     repeat_password: str

class EmpsModel(Base):
    __tablename__ = "employee"

    empid: int = Column(Integer, primary_key=True, index=True)
    empname: str = Column(String, index=True)
    empage: str = Column(String)  
    empsalaray: str = Column(String) 

# class EmpRegistration(Base):
#     __tablename__ = "employee"
#     employeename: str
#     employeeid: int
#     employeeage: str
#     employeesalary: str

class PasswordHashing:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def hash_password(cls, password: str) -> str:
        return cls.pwd_context.hash(password)

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return cls.pwd_context.verify(plain_password, hashed_password)
