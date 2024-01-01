from pydantic import BaseModel
class UserRegistration(BaseModel):
    username: str
    password: str
    repeat_password: str

class EmpRegistration(BaseModel):
    employeename: str
    employeeid: int
    employeeage: str
    employeesalary: str