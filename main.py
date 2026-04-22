from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = False

@app.post('/blog')
def create_blog(request: Blog):
    return {"data": f"Blog is created wit title a {request.title}"}

@app.get('/')
def index():
    return {'data': {"yo": "F"}}

@app.get('/blog/unpublished')
def unpublished():
    return {"data": "unpublished blogs"}



# if __name__ =="__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)