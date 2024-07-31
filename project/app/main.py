from fastapi import Depends, FastAPI
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.db import get_session
from app.models import InputType, UserDataColor

app = FastAPI()

@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/userDatas", response_model=list[UserDataColor])
async def get_user_datas(session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(UserDataColor))
    userDatas = result.all()
    return userDatas

# @app.post("/userData", response_model=UserDataColor)
# async def post_user_data(session: AsyncSession = Depends(get_session)):


# see https://sqlmodel.tiangolo.com/tutorial/automatic-id-none-refresh/
# This could be useful, for example, if you are building a web API to create heroes. And once a hero is created with some data, you return it to the client.
# You wouldn't want to return an object that looks empty because the automatic magic to refresh the data was not triggered.
# In this case, after committing the object to the database with the session, you could refresh it, and then return it to the client. This would ensure that the object has its fresh data.
