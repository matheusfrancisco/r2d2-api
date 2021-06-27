from app.r2d2_engine import suggest_some_rolês
from app.pydantic_types import *
from app.config import settings
from app.models import HealthCheck

from fastapi import FastAPI
import json

app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/healthz")
def run_health_check():
    return HealthCheck()

#TODO: fix user_id and answers input
#TODO  write test to this endpoint
@app.post("/recommendations/{user_id}", response_model=Recommendations)
def recommendations(answers: Answers, user_id: int):
    rolês = suggest_some_rolês(answers=answers, user_id=user_id)
    return rolês
