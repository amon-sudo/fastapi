from fastapi import APIRouter, Depends, HTTPException, Response, status
from .. import models, schemas, database
from typing import List
from sqlalchemy.orm import Session
from ..repositories import blog
from ..oauth2 import get_current_user

router =  APIRouter(
    prefix='/blogs',
    tags=['Blogs']
)

get_db = database.get_db

@router.get('/all', response_model=List[schemas.Amon])
def all(db: Session = Depends(get_db)):
    return blog.get_all(db)

@router.post( '/create', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)

@router.get('/{id}', status_code=200, response_model=schemas.Amon)
def one(id: int, response: Response,db: Session = Depends(get_db)):
    return blog.one(id, db)


@router.delete('/{id}',status_code=status.HTTP_200_OK )
def delete(id: int, db: Session = Depends(get_db)):
    return blog.delete(id, db)
    
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED) 
def put(id:int, request:schemas.Blog, db: Session = Depends(get_db) ):
    return blog.put(id, request, db)

