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
    result = await session.execute(select(InputType))
    songs = result.scalars().all()
    return [InputType(name=song.name, artist=song.artist, year=song.year, id=song.id) for song in songs]


@app.post("/inputTypes")
async def add_song(song: InputTypeCreate, session: AsyncSession = Depends(get_session)):
    song = InputType(name=song.name, artist=song.artist, year=song.year)
    session.add(song)
    await session.commit()
    await session.refresh(song)
    return song