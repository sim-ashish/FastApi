# Query Parameters and String Validations

from fastapi import FastAPI, Query
from typing import Union
from typing_extensions import Annotated    # from typing import Annotated    -> python 3.10+
from pydantic import AfterValidator   # We have a BeforeValidator also



app = FastAPI()


@app.get("/items/")
async def read_items(q: Union[str , None] = None):                             # These are simple validation of data type 
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Performing Additional Validations



@app.get("/getitems/")
async def read_items(q: Annotated[Union[str , None], Query(max_length=50)] = None):                             # Now we are providing validation that it can upto 50 characters 
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Above query is optional because we provide default value

@app.get("/getitems2/")
async def read_items(q: Annotated[str, Query(max_length=50)]):                             # Now we are providing validation that it can upto 50 characters 
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Above we are providing that query is required and validating

''' We can have many validations like
max_length
min_lenght
pattern
default
title
description
alias
deprecated
include_in_schema
'''

# Custom Validation

def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id


@app.get("/items/")
async def read_items(
    id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items()))
    return {"id": id, "name": item}