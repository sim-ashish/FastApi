from pydantic import BaseModel, EmailStr, validator
from typing import List, Union





class User(BaseModel):
    name:str
    email: EmailStr
    password: str

    # @validator('password')
    # def validate_password(cls, value):
    #     if len(value) < 8:
    #         raise ValueError('Password must be at least 8 characters long.')
    #     if not any(char.isdigit() for char in value):
    #         raise ValueError('Password must contain at least one digit.')
    #     if not any(char.isupper() for char in value):
    #         raise ValueError('Password must contain at least one uppercase letter.')
    #     if not any(char.islower() for char in value):
    #         raise ValueError('Password must contain at least one lowercase letter.')
    #     if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/' for char in value):
    #         raise ValueError('Password must contain at least one special character.')
    #     return value

    # def model_post_init(self, __context) -> None:
    #     self.password = hash_password(self.password)
    
''' validato is deprecated we can use field_validator
    @field_validator('password')
    @classmethod
    def validate_password(cls, value: str) -> str:
        if len(value) < 8:
            raise ValueError('Password must be at least 8 characters long.')
        if not any(char.isdigit() for char in value):
            raise ValueError('Password must contain at least one digit.')
        if not any(char.isupper() for char in value):
            raise ValueError('Password must contain at least one uppercase letter.')
        if not any(char.islower() for char in value):
            raise ValueError('Password must contain at least one lowercase letter.')
        if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/' for char in value):
            raise ValueError('Password must contain at least one special character.')
        return value

'''

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List['Blog'] = []

    class Config():
        orm_mode = True


class Blog(BaseModel):
    title: str
    body: str

    class Config():
        orm_mode = True



class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser 

    class Config():
        orm_mode = True



class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None