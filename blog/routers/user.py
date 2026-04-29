
from ..models import User
from ..database import get_db
from ..schemas import User, User1, Amon
from fastapi import Depends
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..repositories import user


from fastapi import APIRouter, HTTPException


router = APIRouter(
    prefix='/Users',
    tags=['Users']
)

get_db = get_db

@router.post( '/', response_model=User1)
def create_user(request:User, db: Session = Depends(get_db)):
    return user.create_user(request, db)


@router.get('/{id}', response_model=User1)
def get_user(id:int, db: Session = Depends(get_db)):
    return user.get_user(id, db)