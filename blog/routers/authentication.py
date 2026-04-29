from fastapi import HTTPException, status
from fastapi import APIRouter, Depends
from fastapi.routing import APIRouter

from sqlalchemy.orm import Session

from blog.hashing import Hash
from ..  import schemas, database, models, token

router = APIRouter(
    prefix='/auth',
    tags=['authentication']
)



@router.post('/')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    
   user = db.query(models.User).filter(models.User.email == request.username).first()
   
   if not user:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                           detail='the user wit that username wasnot found')
       
   if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                           detail='incorrect password')
   access_token = token.create_access_token(data={"sub": user.email})
                             
   return {
       "user":user,
        "access_token": access_token,
        "token_type": "bearer"
    }