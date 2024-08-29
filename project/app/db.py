import os
from sqlmodel import create_engine, Session

DATABASE_URL = os.environ.get("DATABASE_URL")

# Create a synchronous engine
engine = create_engine(DATABASE_URL, echo=True, future=True)

# Dependency that provides a database session
def get_session():
    with Session(engine) as session:
        yield session
