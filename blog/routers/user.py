from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import ShowUser, User 
from .. import models, utils
from .. repository import user as UserRepo

router = APIRouter(
    tags = ['User']
)



@router.get('/users/',response_model=List[ShowUser])
def show_users(db: Session = Depends(get_db)):
    return UserRepo.all(db)


@router.get('/user/{user_id}',response_model=ShowUser)
def show_user(user_id: int, db: Session = Depends(get_db)):
    return UserRepo.retrieve_user(user_id, db)

@router.post('/user/')
def create_user(user: User, db: Session = Depends(get_db)):
    return UserRepo.create(user, db)