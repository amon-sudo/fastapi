

from pydantic import BaseModel





class Blog(BaseModel):
    title: str
    body: str


class Amon(BaseModel):
    title: str
    body: str
    class Config():
        orm_mode = True
        
        
        
class User(BaseModel):
    name: str
    email:str
    password:str
    
    
class User1(BaseModel):
    name: str
    email:str
    
    
    class Config():
        orm_mode = True