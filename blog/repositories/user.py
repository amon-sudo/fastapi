
from ..models import User
from fastapi import HTTPException, status 
from sqlalchemy.orm import Session
from ..hashing import Hash


def create_user(request:User, db: Session):

    new_user = User(name =request.name, email = request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    
    db.refresh(new_user)
    return new_user


def get_user(id:int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    
    if not user:
        raise HTTPException(status_code = 404, detail=f'the user with this if {id} is not found')
    return user