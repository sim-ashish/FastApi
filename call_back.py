from fastapi import FastAPI, Body, BackgroundTasks
from pydantic import BaseModel
import httpx
import asyncio

app = FastAPI()

class RequestPayload(BaseModel):
    callbackUrl: str
    user_id: int

class CallbackPayload(BaseModel):
    message: str
    user_id: int

async def call_client_callback(callback_url: str, user_id: int):
    await asyncio.sleep(3)  # Simulate processing delay
    data = CallbackPayload(message="Processing complete", user_id=user_id)
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(callback_url, json=data.dict())
            print(f"Callback sent. Status: {response.status_code}")
        except Exception as e:
            print(f"Failed to call callback URL: {e}")

@app.post("/start-process")
async def start_process(
    payload: RequestPayload,
    background_tasks: BackgroundTasks
):
    # Start the callback in background
    background_tasks.add_task(call_client_callback, payload.callbackUrl, payload.user_id)
    return {"status": "Processing started", "callback": payload.callbackUrl}
