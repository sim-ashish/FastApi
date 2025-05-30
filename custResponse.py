from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse, ORJSONResponse, PlainTextResponse

app = FastAPI()

class Item(BaseModel):
    name: str
    quant: int

@app.get("/", response_class=PlainTextResponse)
def read_items():
    item = {"name" : "Apple", "quant" : 25, "kashmiri" : True}
    return "hello world"