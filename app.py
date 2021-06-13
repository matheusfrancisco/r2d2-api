from typing import Optional

from fastapi import FastAPI

app = FastAPI()

@app.post("/recommendations")
def recommendations():
    return {"recommendations": [1, 2, 3]}
