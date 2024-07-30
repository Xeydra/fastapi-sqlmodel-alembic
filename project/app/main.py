from fastapi import Depends, FastAPI
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.db import get_session, init_db
from app.models import InputType, InputTypeCreate

app = FastAPI()

@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/inputTypes", response_model=list[InputType])
async def get_songs(session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(InputType))
    inputTypes = result.all()
    return inputTypes

