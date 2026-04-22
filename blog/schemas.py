
from pydantic import BaseModel





class Blog(BaseModel):
    title: str
    body: str


class Amon(BaseModel):
    title: str
    class Config():
        orm_mode = True