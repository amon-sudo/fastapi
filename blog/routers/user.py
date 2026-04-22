
from ..models import User
from ..database import get_db
from ..schemas import User, User1
from fastapi import Depends
from sqlalchemy.orm import Session
from ..hashing import Hash


from fastapi import APIRouter, HTTPException


router = APIRouter()

get_db = get_db

@router.post('/user', response_model=User1, tags=['user'])
def create_user(request:User, db: Session = Depends(get_db)):

    new_user = User(name =request.name, email = request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    
    db.refresh(new_user)
    return new_user


@router.get('/user/{id}', response_model=User1, tags=['user'])
def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    
    if not user:
        raise HTTPException(status_code = 404, detail=f'the user with this if {id} is not found')
    return user