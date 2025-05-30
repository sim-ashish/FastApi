from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://localhost:8000",
    "http://localhost:8000"
]

# allow_origin_regex = ["https://.*\.example\.org"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/")
def read_items():
    return "FastAPI"