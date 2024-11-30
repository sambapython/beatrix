from fastapi import FastAPI, Body
from fastapi.param_functions import Path
from pydantic import BaseModel, Field
from enum import Enum

app = FastAPI()


# @app.post("/items/cat1")
# def items():
#     return {"name": "cat1"}

# class Item(BaseModel):
#     item_id: int
# @app.post("/items/{item}")
# def items(item: Item:
#     return {"name": item}
# valaid_categoriies = ["cat1", "cat2"]
# @app.post("/items/{category}")
# def items(category: str):
#     if category in valaid_categoriies:
#         return {"name": category}
#     else:
#         raise ValueError("Invalid category")
# class ValidCategories(Enum):
#     cat1="cat1"
#     cat2="cat2"
# valaid_categoriies = ["cat1", "cat2"]
# @app.post("/items/{category}")
# def items(category: ValidCategories):
#     return {"name": category}


# @app.post("/items/{item_path}")
# def items(item_path: str):
#     return {"name": item_path}

# @app.post("/items/{item_id}")
# def items(item_id: int, category: str=""):
#     return {"item_id": item_id, "category": category}
#path, query, requestbody 
# class Address(BaseModel):
#     city: str 
#     pin: int 
#     state: str

# class Person(BaseModel):
#     name: str 
#     id: str = Field(strict=False)
#     mobiles: list[str] 
#     #address: Address

# @app.post("/items/{item_id}")
# def items(category: str, item_id: int, pers: Person, dept: int):
    
#     return {"item_id": item_id, "category": category, "pers": pers, "dept": dept}

# class Address(BaseModel):
#     city: str 
#     pin: int 
#     state: str

class Person(BaseModel):
    name: str 
    id: str = Field(strict=False)
    mobiles: list[str] 
    #address: Address

#Person = {"name": "","id":""}


@app.post("/items/{item_id}")
async def items(category: str, item_id: int, dept: int, pers: Person, extra_body: str=Body(embed=True) ):
    
    return {"item_id": item_id, "category": category, "pers": pers, "dept": dept}
