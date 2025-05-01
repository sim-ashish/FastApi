from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import ShowBlog, Blog, User
from .. import models
from .. repository import blog as BlogRepo
from ..oauth2 import get_current_user


router = APIRouter(
    prefix = "/blog",
    tags = ['Blog']
)



@router.get('/', response_model=List[ShowBlog])
def all_blog(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return BlogRepo.get_all(db)


@router.get('/{blog_id}/',  status_code=status.HTTP_200_OK)
def show(blog_id: int,response: Response, db: Session = Depends(get_db)):
    return BlogRepo.get(blog_id, db)


@router.post('/', status_code = status.HTTP_201_CREATED)
def create(blog: Blog, db: Session = Depends(get_db)):
    return BlogRepo.create(blog, db)


@router.put('/{blog_id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(blog_id: int, blog: Blog, db: Session = Depends(get_db)):
    return BlogRepo.update(blog_id, blog, db)

@router.delete('/{blog_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(blog_id: int, db: Session =  Depends(get_db)):
    return BlogRepo.destroy(blog_id, db)