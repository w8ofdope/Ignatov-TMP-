from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Calculation(BaseModel):
    num1: float
    num2: float

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Calculator! You can perform addition, subtraction, multiplication, and division by sending POST requests to the respective endpoints."}

@app.post("/add/")
async def add_numbers(calc: Calculation):
    result = calc.num1 + calc.num2
    return {"operation": "addition", "result": result}

@app.post("/subtract/")
async def subtract_numbers(calc: Calculation):
    result = calc.num1 - calc.num2
    return {"operation": "subtraction", "result": result}

@app.post("/multiply/")
async def multiply_numbers(calc: Calculation):
    result = calc.num1 * calc.num2
    return {"operation": "multiplication", "result": result}

@app.post("/divide/")
async def divide_numbers(calc: Calculation):
    if calc.num2 == 0:
        return {"error": "Division by zero is not allowed"}
    result = calc.num1 / calc.num2
    return {"operation": "division", "result": result}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)