import os
import random 
from time import sleep

import pandas as pd
from fastapi import FastAPI, Depends
from dataclasses import dataclass
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, field_validator, model_validator
import exception_handlers
from typing import Annotated


app = FastAPI()
class Expense(BaseModel):
    description: str 
    amount: float
    category: str
    
# def authenticate():
#     return False
def authenticate():
    print("vallidating authentication")
    yield True 
    print("closing the resources used to authenticate")
    
def get_session():
    print("gettding the db session")
    yield "SESSION"
    print("closing the session")

# class UserAuthentication:
#     # def __init__(self, name):
#     #     self.name=name
#     def __call__(self):
#         return True   
#     @classmethod
#     def get_seesion(cls, name):
#         return name

class UserAuthenitcate:
    def __init__(self, name):
        self.name = name
        
    def __call__(self):
        return self.name

u1=UserAuthenitcate("HELLO")
@app.post("/expenses", )
def expenses(data: Expense, is_authenticate: Annotated[bool, Depends(u1)],
             session: Annotated[str, Depends(get_session)]):
    print("PROCCESING EXPENSES")
    if is_authenticate:
        print("Authentication failed")
        return {"msg": "success"}
    else:
        print("Authentication SUCCESSFUL")
        return {"msg": "FAILED"}
    
print("PROCCESING EXP")
    
    

@app.exception_handler(Exception)
async def exceptions_handler(request, exception):
    return exception_handlers.python_exception_handler(exception)
    

class Employee(BaseModel):
    id: int 
    department: str = Field(pattern="[a-zA-z]+")
    name: str = Field(pattern='[a-zA-Z_0-9]+')
    salary: int = Field(gt=100000, le=10000000)
    
    @field_validator('salary')
    def validate_salary(cls, value):
        print("SALARY VALIDATION CALLED")
        if value > 7000000:
            raise ValueError("value must less than 7000000")
        return value
    
    # @field_validator("department")
    # def validate_department(cls, value):
    #     return value.upper()
    
    
        
    @model_validator(mode='after')
    def validate(self):
        print("MODEL VALIDATION CALLEDDDDDDDDDDDDDDDDDDDDDD")
        if 'admin' in self.department:
            if self.salary > 1000000:
                raise ValueError("salary must be less than 1000000")
        self.department = self.department.upper()
        return self
            
                
        
          
@app.post('/employee/', status_code=201)
def save_data(data:Employee):
    # if not data.validate():
    #     error = {"message": "Name must not contain special characters"}
    #     return JSONResponse(status_code=400, content=error)
    # add_data_to_employee_file(data.__dict__)
    return {'data': data}

def save_data_into_employee_file(f,i):
    print(threading.active_count())
    row = f"{i},{fak.name()},{random.choice(dept_ids)}"
    f.write(row)
    f.write("\n")
    f.flush()
    
def add_data_to_employee_file(data):
    row = f"{data['emp_id']},{data['name']},{data['department_id']}"
    file_path = os.path.join("data","employee.csv")
    with open(file_path, "a") as f:
        f.write(row)
        f.write("\n")



def get_department_ids():
    df = pd.read_csv('departments.csv')
    return df.id.values



@app.get("/randomDepartment")
def getRandomDepartment():
    # try:
    depts = get_department_ids()
    print("processing")
    raise Exception("EXFEPTION")
    # except Exception as err:
    #     print("*"*100)
    #     print(err)
    #     return {"Error": str(err)}
    # except:
    #     return {"Error:EXCEPT": str(err)}
    return {"dept_id": int(random.choice(depts))}
        

# class Employee:
#     def __init__(self, emp_id,name,department_id):
#         self.name=name
#         self.emp_id=emp_id
#         self.dept_id=department_id

# @dataclass
# class Employee:
#     name: str
#     emp_id: int 
#     department_id: int
    
#     def __init__(self, name: str, emp_id:int,  department_id: int):
#         print("INIT INVOKEDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
#         if not self.name.isalnum():
#             raise ValueError("Invalid name")
#         self.name = name
#         self.emp_id = emp_id
#         self.department_id = department_id
    
#     def validate(self):
#         # if not self.name.isalnum():
#         #     raise ValueError("Name must not contains special symbols")
#         return self.name.isalnum()



# @app.post('/employee/{employee_id}')
# def save_data(employee_id: int):
#     #add_data_to_employee_file({"name":name,"department_id":department_id,"id":emp_id})
#     return {'id': employee_id}
    
# @app.get('/employee')
# def save_data(emp_id: int, name: str, department_id:int):
#     add_data_to_employee_file({"name":name,"department_id":department_id,"id":emp_id})
#     return {'name': name, 'department_id':department_id,'id': department_id}
    

@app.get("/users")
def get_user():
    return {"name":" HELLO"}
    