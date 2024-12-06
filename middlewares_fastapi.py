from fastapi import FastAPI
from pydantic import BaseModel
from findmyIP import get_county
import numpy 
from fastapi.responses import JSONResponse
ar1=numpy.array([1,2,3,4])

app = FastAPI()
class Expense(BaseModel):
    description: str 
    amount: float
    category: str
    
class Category:
    def __init__(self, name):
        self.name=name
    
class Employee:
    def __init__(self, name, cat_name):
        self.emp_name=name
        self.category = Category(name=cat_name)
        self.categories = [Category(name=cat_name), Category(name=cat_name)]
        self.cat_data = {"cates": [Category(name=cat_name), Category(name=cat_name)]}
    
    
@app.middleware("http")
def IPcheck(request, call_next):
    resp = get_county('152.59.199.179')
    country = resp.text.strip()
    print("*"*50)
    print(country)
    if country=="IN":
        resp = call_next(request)
    else:
        resp = JSONResponse(status_code=400, content={"error": "OUT OF THE COUNTRY REQUEST"})
    return resp
    
    
@app.post("/expenses", )
async def expenses(data: Expense):
    emp = Employee(name="name1", cat_name="cat1")
    #return {"data": emp}
    return {"data": "expenses"}

@app.post("/expenses1", )
async def expenses12(data: Expense):
    emp = Employee(name="name1", cat_name="cat1")
    # return {"data": emp}
    return {"data": "expenses1"}

@app.post("/expenses2", )
async def expenses(data: Expense):
    emp = Employee(name="name1", cat_name="cat1")
    # return {"data": emp}
    return {"data": "expenses2"}


    # emp = Employee(name="name1", cat_name="cat1")
    # #{"data": emp, "ar1": "ar1"}
    # #return {"data": emp}
    # resp = get_county('49.204.99.131')
    # country = resp.text.strip()
    # if country=="IN":
    #     return {"data": resp.text.strip()}
    # else:
    #     #prepare a custom response with 400 status code
    #     return {"data": ""}
    