from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Operation(BaseModel):
    number1: float
    number2: float

@app.post("/add/")
def add(operation: Operation):
    return {"result": operation.number1 + operation.number2}

@app.post("/subtract/")
def subtract(operation: Operation):
    return {"result": operation.number1 - operation.number2}

@app.post("/multiply/")
def multiply(operation: Operation):
    return {"result": operation.number1 * operation.number2}

@app.post("/divide/")
def divide(operation: Operation):
    if operation.number2 == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result": operation.number1 / operation.number2}
