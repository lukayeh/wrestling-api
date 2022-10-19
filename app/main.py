import json
from os.path import dirname
from typing import Optional

from app.api import api
from fastapi import FastAPI, HTTPException

app = FastAPI()

with open(dirname(__file__) + "/pkg_info.json") as fp:
    info = json.load(fp)

__version__ = info["version"]


@app.get("/")
async def root():
    return {"message": "Wrestler API in Python", "version": __version__}


# Get wrestler inclusive of ID query and search by.
@app.get("/wrestler")
async def get_wrestler(id: Optional[int] = None, name: Optional[str] = None):

    # Error if trying to search by both!
    if name and id:
        raise HTTPException(
            status_code=400,
            detail="Cannot query by NAME and ID at the same time",  # noqa: E501
        )
    # Filter by id
    elif id:
        wrestler = api.get_wrestler(id)

        if not wrestler:
            raise HTTPException(status_code=400, detail="Error")

        return wrestler
    # Search data by name
    elif name:
        wrestlers = api.search_wrestler(name)

        if not wrestlers:
            raise HTTPException(status_code=400, detail="Error")

        return wrestlers

    # Default returns all
    return api.read_wrestler()
