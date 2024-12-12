from fastapi import APIRouter

r1 = APIRouter()

@r1.get("/users/")
def get_exeenses():
    return {"resp": "user1"}