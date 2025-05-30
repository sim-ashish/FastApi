from fastapi import FastAPI, HTTPException, Request

from fastapi.responses import JSONResponse

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},
        )
    return {"item": items[item_id]}


# Install custom exception handlers
'''
You can add custom exception handlers with the same exception utilities from Starlette.

Let's say you have a custom exception UnicornException that you (or a library you use) might raise.

And you want to handle this exception globally with FastAPI.

You could add a custom exception handler with @app.exception_handler():
'''


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )



@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}