import os
import random 

import pandas as pd
from fastapi import FastAPI
from dataclasses import dataclass
from fastapi.responses import JSONResponse


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

app = FastAPI()

def get_department_ids():
    df = pd.read_csv('departments.csv')
    return df.id.values

@app.get("/randomDepartment")
def getRandomDepartment():
    depts = get_department_ids()
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


    
    
    
    def validate(self):
        # if not self.name.isalnum():
        #     raise ValueError("Name must not contains special symbols")
        return self.name.isalnum()
        
            
        
        
@app.post('/employee/', status_code=201)
def save_data(data: Employee):
    if not data.validate():
        error = {"message": "Name must not contain special characters"}
        return JSONResponse(status_code=400, content=error)
    add_data_to_employee_file(data.__dict__)
    return {'data': data}

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
    