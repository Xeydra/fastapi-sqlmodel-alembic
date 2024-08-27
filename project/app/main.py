from fastapi import Depends, FastAPI
from sqlmodel import select
from sqlalchemy.orm import Session, selectinload
from app.db import get_session
from app.models import UserDataBase, UserQuestionBase, userQuestionModels, userDataModels

app = FastAPI()

@app.get("/ping")
def pong():
    return {"ping": "pong!"}


@app.get("/userQuestions", response_model=list[UserQuestionBase])
def get_user_questions(session: Session = Depends(get_session)):
    all_entries = []
    print(session)
    for model in userQuestionModels:
        result = session.query(model).options(selectinload(model.answer_set))
        all_entries.extend(result.all())
    return all_entries

@app.get("/userDatas", response_model=list[UserDataBase])
def get_user_datas(session: Session = Depends(get_session)):
    all_entries = []
    # for model in userDataModels:
    #     result = session.exec(select(model))
    #     all_entries.extend(result.all())
    return all_entries

# @app.post("/userData", response_model=UserDataBase)
# async def post_user_data(userDataCreate: UserDataColorCreate, session: AsyncSession = Depends(get_session)):
#     db_userDataCreate = UserDataBase.model_validate(userDataCreate)
#     session.add(db_userDataCreate)
#     await session.commit()
#     await session.refresh(db_userDataCreate)
#     return db_userDataCreate



# see https://sqlmodel.tiangolo.com/tutorial/automatic-id-none-refresh/
# This could be useful, for example, if you are building a web API to create heroes. And once a hero is created with some data, you return it to the client.
# You wouldn't want to return an object that looks empty because the automatic magic to refresh the data was not triggered.
# In this case, after committing the object to the database with the session, you could refresh it, and then return it to the client. This would ensure that the object has its fresh data.
