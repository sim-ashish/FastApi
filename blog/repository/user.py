from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas, utils

def all(db: Session):
    users = db.query(models.User).all()
    return users


def retrieve_user(user_id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"User with id {user_id} not exist")
    return user


def create(user: schemas.User, db: Session):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = models.User(
        **user.dict(exclude={'password'}), 
        password=utils.hash_password(user.password) 
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

