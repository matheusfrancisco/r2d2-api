"""
Any Pydantic models live here.
See: https://pydantic-docs.helpmanual.io/usage/models/
if this file start to grow fast we should split specific models
each in your file
"""
from pydantic import BaseModel


class HealthCheck(BaseModel):
    status: str = "ok"
