from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI

app = FastAPI()
@app.get("/")
async def home():
    return {"message": f"Hello RKE2! dari branch demo"}
