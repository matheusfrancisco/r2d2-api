from fastapi import FastAPI

from app.config import settings
from app.models.establishment import establishments
from app.adapters.out.establishments import out_establishments
from app.adapters.out.recommendations import out_recommendations
from app.logic.engine import recommendations


app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)


@app.get("/alive")
def run_health_check():
    return {'ok':'ok'}


@app.get("/establishments")
def all_establishments():
    e = out_establishments(establishments())
    return {"establishments": e}


@app.post("/recommendations/{user_id}")
def recommendations():
    e = out_recommendations(establishments())
    return {"recommendations": e}

@app.post("/v1/recommendations/{user_id}")
def v1_recommendations():
    #e = out_recommendations(establishments())
    e = recommendations()
    return {"recommendations": e}
