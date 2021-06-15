from pydantic import BaseModel
from typing import List

class User_id(BaseModel):
    id: float

class Immediate_user_preferences(BaseModel):
    how_much: int
    like: int
    number_of_ppl: int

class Recommendations(BaseModel):
    top_recommended_ids: List[float]