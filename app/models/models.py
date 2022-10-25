from typing import Optional

from pydantic import BaseModel

from fastapi import Query


class Item(BaseModel):
    name: str
    billFrom: str
    signatureMoves: list
    finishingMoves: list
    dob: str
    works_for: str
    birthName: str
    nickNames: list


class Querymodel(BaseModel):
    name: Optional[str] = Query(None)
    billFrom: Optional[str] = Query(None)
    signatureMoves: Optional[str] = Query(None)
    finishingMoves: Optional[str] = Query(None)
    dob: Optional[str] = Query(None)
    works_for: Optional[str] = Query(None)
    birthName: Optional[str] = Query(None)
    nickNames: Optional[str] = Query(None)
