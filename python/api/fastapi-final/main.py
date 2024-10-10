from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

elements: List[str] = []

@app.get("/sum1n/{n}")
def sum1n(n: int):
    return {"result": sum(range(1, n + 1))}

@app.get("/fibo")
def fibonacci(n: int):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return {"result": a}

@app.post("/reverse")
def reverse_string(string: str):
    return {"result": string[::-1]}

@app.put("/list")
def add_to_list(element: str):
    elements.append(element)
    return {"result": elements}

@app.get("/list")
def get_list():
    return {"result": elements}

@app.post("/calculator")
def calculate(expr: str):
    try:
        num1, operator, num2 = expr.split(',')
        num1, num2 = float(num1), float(num2)
    except ValueError:
        raise HTTPException(status_code=400, detail="invalid")

    if operator == '+':
        return {"result": num1 + num2}
    elif operator == '-':
        return {"result": num1 - num2}
    elif operator == '*':
        return {"result": num1 * num2}
    elif operator == '/':
        if num2 == 0:
            raise HTTPException(status_code=403, detail="zerodiv")
        return {"result": num1 / num2}
    else:
        raise HTTPException(status_code=400, detail="invalid")
