# When you need to receive form fields instead of JSON, you can use Form.
# install python-multipart

from typing_extensions import Annotated

from fastapi import FastAPI, Form, Body
from pydantic import BaseModel

app = FastAPI()


@app.post("/login/")
def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username, "password" : password}

'''
Data from forms is normally encoded using the "media type" application/x-www-form-urlencoded.
'''


# You can use Pydantic models to declare form fields in FastAPI.



class FormData(BaseModel):
    username: str
    password: str
    model_config = {"extra": "forbid"}


@app.post("/loginuser/")
async def login(data: Annotated[FormData, Form()]):
    return data