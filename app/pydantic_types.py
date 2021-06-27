from pydantic import BaseModel
from typing import List

class Answers(BaseModel):
    how_much: int
    like: int
    number_of_ppl: int

class Recommendations(BaseModel):
    top_recommended_ids: List[float]
    top_recommended_names: List[str]