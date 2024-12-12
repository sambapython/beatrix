from fastapi import APIRouter

router = APIRouter()

@router.get("/client_exepnses1/")
def get_exeenses():
    return {"resp": "sadfsad"}