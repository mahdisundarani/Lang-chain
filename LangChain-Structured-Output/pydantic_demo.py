from pydantic import BaseModel,EmailStr,Field
from typing import Optional 
class Student (BaseModel):
    name: str = 'Unknown'
    age: Optional[int] 
    email: EmailStr
    cgpa: Optional[float] = Field(None, ge=0.0, le=10.0)

new_student = {"name": "Mahdi", "age": 30, "email": "mahdi@gmail.com","cgpa": 8.5}

student = Student(**new_student)

print(student)
print(type(student))

