
# Query Parameter Models
'''If you have a group of query parameters that are related, you can create a Pydantic model to declare them.'''

from typing_extensions import Annotated
from typing import Literal , List

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()


class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: List[str] = []


@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):       # http://127.0.0.1:8000/items/?limit=100&offset=2&order_by=updated_at&tags=cool
    return filter_query