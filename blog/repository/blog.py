from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def get(blog_id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail' : f"Blog with id {blog_id} not exist"}
        # Instead of above we can use HTTPException
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Blog with id {blog_id} not exist")
    
    return blog


def create(blog: schemas.Blog, db: Session):
    new_blog = models.Blog(title = blog.title, body = blog.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def update(blog_id: int, blog: schemas.Blog, db: Session):
    blog_obj = db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not blog_obj.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Blog with id {blog_id} not exist")
    blog_obj.update(blog.model_dump(), synchronize_session=False)
    db.commit()
    return blog_obj.first()


def destroy(blog_id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Blog with id {blog_id} not exist")
    blog.delete(synchronize_session = False)
    db.commit()
    return {'detail' : 'success'}