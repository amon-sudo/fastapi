from urllib import response

from fastapi import FastAPI, Depends, status, Response, HTTPException
from sentry_sdk import session
from . import schemas,  models
from sqlalchemy.orm import Session

from .database import engine, sessionLocal
import blog
app = FastAPI()


models.Base.metadata.create_all(engine)


def get_db():
    db = sessionLocal()
    try:
        yield db
        
    finally:
        db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return new_blog


@app.get('/blog')
def all(db: Session = Depends(get_db)):
    
    blogs = db.query(models.Blog).all()
    
    
    return blogs


@app.get('/blogs/{id}', status_code=200, response_model=schemas.Blog)
def one(id: int, response: Response,db: Session = Depends(get_db) ):
    
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code = 404, detail=f'the blog with this if {id} is not found')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'error': f'this blog was not found with id {id}'}
    return blogs


@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT )
def delete(id: int, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'
    
@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED) 
def put(id:int, request:schemas.Blog, db: Session = Depends(get_db) ):
    nn = db.query(models.Blog).filter(models.Blog.id == id).update(request.model_dump())
    db.commit()
    if not nn:
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED, detail='nothing has happened')
        
    return 'updated succesflly'