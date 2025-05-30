from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")
async def add_timer(request: Request, call_next):     # we have to use async because response will be a coroutine
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = start_time - time.perf_counter()
    response.headers["X-Process-Time"] = str(process_time)
    print("Process Time:", process_time)
    return response


@app.get("/")
def read_items():
    return "FastAPI"