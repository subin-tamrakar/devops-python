from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Calculator API"}

@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}

@app.get("/sub")
def sub(a: float, b: float):
    return {"result": a - b}

@app.get("/mul")
def mul(a: float, b: float):
    return {"result": a * b}

@app.get("/div")
def div(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero")
    return {"result": a / b}
