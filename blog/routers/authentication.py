from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import schemas, models, utils
from ..database import get_db
from datetime import timedelta
from ..Jwttoken import create_access_token

router = APIRouter(
    tags = ['Authentication']
)

@router.post('/login')
def login(login: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == login.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
    
    if utils.verify_password(login.password, user.password):

        access_token = create_access_token(data={"sub": user.email})
        return schemas.Token(access_token=access_token, token_type="bearer")
    
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")