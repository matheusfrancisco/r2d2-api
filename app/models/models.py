try:
    import unzip_requirements
except ImportError:
    Exception("there was a problem with imports")
"""
DEPRECATED FILE
it will be refactor
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
