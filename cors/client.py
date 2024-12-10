from fastapi import FastAPI 
import requests


app = FastAPI()

@app.get("/client_exepnses/")
def get_exeenses():
    resp = requests.post("http://localhost:8000/expenses")
    return {"resp": resp.json()}