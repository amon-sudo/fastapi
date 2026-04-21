from fastapi import  FastAPI

from pydantic import BaseModel




app = FastAPI()



class Blog(BaseModel):
    pass
    
@app.post('/blog')
def create_blog(requet: Blog):
    return {}
    



@app.get('/')
def index():
    return {'data':{"yo":"F"}}




@app.get('/blog/unpublised')
def unpublished():
    return {"unpublished"}