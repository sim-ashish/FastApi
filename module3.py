from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union


class Item(BaseModel):
    name : str
    # description : str | None = None     # for python > 3.10
    description : Union[str, None] = None
    price : float
    # tax : float | None = None       # for python > 3.10
    tax : Union[float, None] = None    # we are providing default value


app = FastAPI()

@app.post("/items/")
def create_item(item: Item):
    
    return item


@app.post("/items2/")
def create_item(item: Item):
    item_dict = item.dict()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}       




