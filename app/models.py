"""
Any Pydantic models live here.
See: https://pydantic-docs.helpmanual.io/usage/models/
if this file start to grow fast we should split specific models
each in your file
"""
from pydantic import BaseModel
from typing import List


class HealthCheck(BaseModel):
    status: str = "ok"

class Answers(BaseModel):
    how_much: int
    like: int
    number_of_ppl: int

class Recommendations(BaseModel):
    top_recommended_ids: List[str]