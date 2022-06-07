from lib2to3.pytree import Base
from pydantic import BaseModel

class TreeNew(BaseModel):
    Name:str
    val:int

    class Config:
        orm_mode=True

class TreeNewCreate():
    id:int

class NodeNew(BaseModel):
    tree_id:int
    