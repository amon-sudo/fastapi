

from pydantic import BaseModel

from typing import List



class Blog(BaseModel):
    title: str
    body: str


  
        
class User(BaseModel):
    name: str
    email:str
    password:str
    
    
class User1(BaseModel):
    name: str
    email:str
    blogs : List[Blog] = []
    
    
    class Config():
        orm_mode = True
        
        
class Amon(BaseModel):
    title: str
    body: str
    creator: User1
    class Config():
        orm_mode = True
        
class Login(BaseModel):
     username: str
     password: str