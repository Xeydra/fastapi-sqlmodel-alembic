import os
from sqlmodel import SQLModel, create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.environ.get("DATABASE_URL")

# Create a synchronous engine
engine = create_engine(DATABASE_URL, echo=True, future=True)

# Create a sessionmaker bound to the synchronous engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables and initialize the database
def init_db():
    with engine.begin() as conn:
        SQLModel.metadata.create_all(conn)

# Dependency that provides a database session
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
