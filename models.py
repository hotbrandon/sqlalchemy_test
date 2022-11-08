from pydantic import BaseModel
from typing import Optional, List


class ModelD(BaseModel):
    d_name: str


class ModelM(BaseModel):
    name: str
    d: List[ModelD] = []
