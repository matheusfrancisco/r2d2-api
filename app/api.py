from app.r2d2_engine import suggest_some_rolês
from app.models import *
from app.config import settings

from mangum import Mangum
from fastapi import FastAPI, Body

app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)
handler = Mangum(app)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/healthz")
def run_health_check():
    return HealthCheck()

#TODO: fix user_id and answers input
#TODO  write test to this endpoint
@app.post("/recommendations/{user_id}", response_model=Recommendations)
def recommendations(user_id: int, answers: Answers):
    rolês = suggest_some_rolês(answers=answers, user_id=user_id)
    rolês = {
        "top_recommended_ids": rolês
    }
    return rolês

