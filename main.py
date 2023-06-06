import time
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Now Time:" + time.time()}
