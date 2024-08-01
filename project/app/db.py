import os

from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

from sqlalchemy.orm import sessionmaker


DATABASE_URL = os.environ.get("DATABASE_URL")

# echo: print all sql statements, probably remove in production
# sqlmodels create engine same as sqlalchemys, just that future=true is default
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# here all models are created
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session