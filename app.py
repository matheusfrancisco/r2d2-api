from fastapi import FastAPI
import json
from src.r2d2_engine import suggest_some_rolês
from src.pydantic_types import *

app = FastAPI()

#TODO: fix user_id and answers input
@app.post("/recommendations", response_model=Recommendations)
def recommendations(user_id: User_id, answers: Immediate_user_preferences) -> json:
    rolês = suggest_some_rolês(user_id=user_id, answers=answers)
    return rolês
