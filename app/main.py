import json
from os.path import dirname

from app.api import api
from app.models import models
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

with open(dirname(__file__) + "/pkg_info.json") as fp:
    info = json.load(fp)

__version__ = info["version"]


@app.get("/")
async def root():
    return {"message": "Wrestler API in Python", "version": __version__}


# Search by model!.
@app.get("/wrestler")
async def get_wrestler(queries: models.Querymodel = Depends()):
    wrestlers = api.query_wrestler(queries)

    if not wrestlers:
        raise HTTPException(status_code=400, detail="Error")

    return json.loads(wrestlers)


@app.post("/wrestler")
async def create_wrestler(item: models.Item):
    wrestler = api.create_wrestler(item)
    return wrestler
