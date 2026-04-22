from fastapi import APIRouter, Depends, HTTPException, Response, status
from .. import models, schemas, database
from typing import List
from sqlalchemy.orm import Session



router =  APIRouter()

get_db = database.get_db

@router.get('/blog', response_model=List[schemas.Amon], tags=['blogs'])
def all(db: Session = Depends(database.get_db)):
    
    blogs = db.query(models.Blog).all()
    
    
    return blogs


@router.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return new_blog


# @router.get('/blog', response_model=List[schemas.Amon], tags=['blogs'])
# def all(db: Session = Depends(get_db)):
    
#     blogs = db.query(models.Blog).all()
    
    
#     return blogs


@router.get('/blogs/{id}', status_code=200, response_model=schemas.Amon, tags=['blogs'])
def one(id: int, response: Response,db: Session = Depends(get_db) ):
    
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code = 404, detail=f'the blog with this if {id} is not found')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'error': f'this blog was not found with id {id}'}
    return blogs


@router.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'] )
def delete(id: int, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'
    
@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs']) 
def put(id:int, request:schemas.Blog, db: Session = Depends(get_db) ):
    nn = db.query(models.Blog).filter(models.Blog.id == id).update(request.model_dump())
    db.commit()
    if not nn:
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED, detail='nothing has hrouterened')
        
    return 'updated succesflly'

