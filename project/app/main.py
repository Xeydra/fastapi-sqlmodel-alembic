from fastapi import Depends, FastAPI
from sqlmodel import select, Session
from sqlalchemy.orm import selectinload
from app.db import get_session
from app.models import UserQDataBase, AnswerSetColor, userQuestionModels, userDataModels, UserQDataColorCreate, UserQuestionBaseRead, UserQDataColor

app = FastAPI()

@app.get("/ping")
def pong():
    return {"ping": "pong!"}


@app.get("/userQuestions", response_model=list[UserQuestionBaseRead])
def get_user_questions(session: Session = Depends(get_session)):
    all_entries = []
    for model in userQuestionModels:
        result = session.exec(select(model).options(selectinload(model.answer_set)))
        all_entries.extend(result.all())
    return all_entries

@app.post("/userQData", response_model=UserQDataBase)
def createUserQData(userData: UserQDataColorCreate, session: Session = Depends(get_session)):
    answer = session.exec(select(AnswerSetColor).where(AnswerSetColor.id == userData.value)).first()
    new_user_q_data = UserQDataColor(user_question_id = userData.user_question_id, value = answer.value, for_date = userData.for_date)
    session.add(new_user_q_data)
    session.commit()
    session.refresh(new_user_q_data)
    return new_user_q_data

@app.get("/userQData/{user_question_id}", response_model=list[UserQDataBase])
def createUserQData(user_question_id: int, session: Session = Depends(get_session)):
    all_entries = []
    for model in userDataModels:
        result = session.exec(select(model).where(model.user_question_id == user_question_id))
        all_entries.extend(result.all())
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
