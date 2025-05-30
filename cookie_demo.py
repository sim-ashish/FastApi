from fastapi import FastAPI, Cookie, Header
from typing_extensions import Annotated
from typing import Union

app = FastAPI()

@app.get("/")
def read_items(ads_id: Annotated[Union[str, None], Cookie()] = None):
    print("ADS ID : ", ads_id)
    return {"Cookie Ads id" : ads_id}

# We have to set cookie in browser, Docs cookie will not work 


@app.get("/headers")
def read_items(user_agent: Annotated[Union[str, None], Header()] = None):
    return {"User-Agent": user_agent}

# Headers

'''
Header has a little extra functionality on top of what Path, Query and Cookie provide.

Most of the standard headers are separated by a "hyphen" character, also known as the "minus symbol" (-).

But a variable like user-agent is invalid in Python.

So, by default, Header will convert the parameter names characters from underscore (_) to hyphen (-) to extract and document the headers.

Also, HTTP headers are case-insensitive, so, you can declare them with standard Python style (also known as "snake_case").

So, you can use user_agent as you normally would in Python code, instead of needing to capitalize the first letters as User_Agent or something similar.

If for some reason you need to disable automatic conversion of underscores to hyphens, set the parameter convert_underscores of Header to False:
'''

# Duplicate headers
'''
It is possible to receive duplicate headers. That means, the same header with multiple values.

You can define those cases using a list in the type declaration.

You will receive all the values from the duplicate header as a Python list.

For example, to declare a header of X-Token that can appear more than once, you can write:
'''


@app.get("/items/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}


# We can also use Pydantic model for cookie and headers
'''
class Cookies(BaseModel):
    model_config = {"extra": "forbid"}

    session_id: str
    fatebook_tracker: Union[str, None] = None
    googall_tracker: Union[str, None] = None


@app.get("/items/")
async def read_items(cookies: Annotated[Cookies, Cookie()]):
    return cookies

'''


# Same for headers

'''
class CommonHeaders(BaseModel):
    model_config = {"extra": "forbid"}

    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@app.get("/items/")
async def read_items(headers: Annotated[CommonHeaders, Header()]):
    return headers


@app.get("/items/")
async def read_items(
    headers: Annotated[CommonHeaders, Header(convert_underscores=False)],
):
    return headers
'''