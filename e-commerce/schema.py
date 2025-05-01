from pydantic import BaseModel
from typing import Union

class Category(BaseModel):
    title : str
    description : str

class Product(BaseModel):
    category : Category
    name : str
    price : float
    description : Union[str, None] = None
    rating : int = 0
    