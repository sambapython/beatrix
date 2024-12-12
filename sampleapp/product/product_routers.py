from fastapi import APIRouter
from fastapi import FastAPI, Depends

router = APIRouter()

#products/

def api_dependencies():
    print("CALLED API DEPENDENCY")
    return None

@router.post("/product/")
def product_create():
    return {"resp": "product"}

# @router.get("/product/",dependencies=[Depends(api_dependencies)])
@router.get("/product/",dependencies=[])
def product_create():
    return {"resp": "product"}

@router.put("/product/")
def product_create():
    return {"resp": "product"}