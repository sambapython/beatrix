from fastapi import FastAPI, Depends, BackgroundTasks
import requests
from main1 import router as main1_router
from product import product_routers
from users import  user_routers
import constants as c
from time import sleep
import threading

def all_depends():
    print("CALLED ALL DEPENDENCIES")
    return True

# how to exclude few APIs from app dependencies..
# can we add some dependencies inside the include_router
app = FastAPI(dependencies=[Depends(all_depends)])
sub_app = FastAPI()

def calculate_statement():
    c=0
    data = []
    while True:
        c=c+1
        data.append(c)
        sleep(1)
        print("*"*20)
        print("processing statement")
        if c==120:
            break
    return data

@app.get('/statement', )
def statement(bakc_jobs: BackgroundTasks):
    #bakc_jobs.add_task(calculate_statement)
    threading.Thread(target=calculate_statement)
    return {"statement":"statemetb is in progress"}
    


@app.get("/client_exepenses/")
def get_exeenses():
    return {"resp": "fdsafsa"}

def router_dependencies():
    print("CALLED ROUTER DEPENDENCY")
    return None

app.include_router(main1_router)
app.include_router(user_routers.r1, tags=["USERS", "USERS1"])
sub_app.include_router(product_routers.router, 
                   prefix=c.PRODUCT_PREFIX,
                   dependencies=[Depends(router_dependencies)],
                   tags=["PRODUCT","PURCHASE", "SALES"])

@app.get("/items")
def get_items():
    return {"resp": "items"}

# @app.get("/items/{name}")
# def get_items(name: str, ):
#     return {"resp": "items:"+name}