from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse
from typing import Union

app = FastAPI()


@app.get("/portal", response_model = None)
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}