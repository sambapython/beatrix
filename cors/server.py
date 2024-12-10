from fastapi import FastAPI 


app = FastAPI()

@app.post("/expenses/")
def exepenses():
    return {"data": "expenses"}
    