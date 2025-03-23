from fastapi import FastAPI
from calcu.adder import Adder


app = FastAPI()


@app.get("/api/v1/add")
def add(a: int, b: int) -> int:
    adder = Adder(a, b)
    return adder.execute()
