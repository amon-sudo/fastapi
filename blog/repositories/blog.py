
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status,Response
from ..models import Blog
from .. import schemas, models


def get_all(db: Session):
    blogs = db.query(Blog).all()
    return blogs

def create(request: schemas.Blog, db: Session ):
    new_blog = models.Blog(title=request.title, body = request.body, user_id=models.user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return new_blog
    
    
def delete(id: int, db: Session):
    hey = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    if not hey:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='the above blog was not found')
    db.commit()
    return {"message":"deleted succesfully"}
    
    
def put(id:int, request:schemas.Blog, db: Session ):
    nn = db.query(models.Blog).filter(models.Blog.id == id).update(request.model_dump())
    db.commit()
    if not nn:
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED, detail='nothing has hrouterened')
        
    return 'updated succesflly'


def one(id: int, response: Response,db: Session ):
    
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = 404, detail=f'the blog with this if {id} is not found')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'error': f'this blog was not found with id {id}'}
    return blog