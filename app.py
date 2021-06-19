from fastapi import FastAPI
import json
from src.r2d2_engine import suggest_some_rolês
from src.pydantic_types import *

app = FastAPI()

#TODO: fix user_id and answers input
@app.post("/recommendations/{user_id}", response_model=Recommendations)
def recommendations(answers: Answers, user_id: int):
    rolês = suggest_some_rolês(answers=answers, user_id=user_id)
    return rolês