from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import TypeVar, Generic
#
##
### BASEMODELS
##
#
typeAny = TypeVar("T")

class UserQuestionBase(SQLModel):
    question_text: str
    created_at: datetime = Field(default=datetime.now(), nullable=False)
    updated_at: datetime | None = Field(default=None)
    deleted_at: datetime | None = Field(default=None)

class UserQuestionAnswerSetLinkBase(SQLModel):
    pass

class UserQDataBase(Generic[typeAny], SQLModel):
    value: typeAny
    for_date: datetime | None = Field(default=datetime.now(), nullable=False)

class UserQDataBaseTable(UserQDataBase[typeAny]):
    created_at: datetime = Field(default=datetime.now(), nullable=False)
    updated_at: datetime | None = Field(default=None)
    deleted_at: datetime | None = Field(default=None)

class UserQDataCreate(UserQDataBase[typeAny]):
    user_question_id: int
    pass

class AnswerSetBase(Generic[typeAny], SQLModel):
    label: str | None
    value: typeAny
    created_at: datetime = Field(default=datetime.now(), nullable=False)
    deleted_at: datetime | None = Field(default=None)

class AnswerSetBaseRead(AnswerSetBase[typeAny]):
    pass

class UserQuestionBaseRead(UserQuestionBase):
    answer_set: list[AnswerSetBaseRead]

#
##
### COLORS
##
#
class UserQuestionColorLink(UserQuestionAnswerSetLinkBase, table=True):
    user_question_id: int = Field(foreign_key="userquestioncolor.id", nullable=False, primary_key=True)
    answer_set_id: int = Field(foreign_key="answersetcolor.id", nullable=False, primary_key=True)

class AnswerSetColor(AnswerSetBase[str], table=True):
    id: int | None = Field(default=None, nullable=False, primary_key=True)
    value: str = Field(..., index=True, unique=True, regex=r'^#[0-9A-Fa-f]{6}$')
    
    user_questions: list["UserQuestionColor"] = Relationship(back_populates="answer_set", link_model=UserQuestionColorLink)

class UserQuestionColor(UserQuestionBase, table=True):
    id: int | None = Field(default=None, nullable=False, primary_key=True)
    
    answer_set: list["AnswerSetColor"] = Relationship(back_populates="user_questions", link_model=UserQuestionColorLink)
    user_q_datas: list["UserQDataColor"] = Relationship(back_populates="user_question")

class UserQDataColor(UserQDataBaseTable[str], table=True):
    id: int | None = Field(default=None, nullable=False, primary_key=True)
    value: str = Field(..., index=True, regex=r'^#[0-9A-Fa-f]{6}$')

    user_question_id: int = Field(foreign_key="userquestioncolor.id", nullable=False)
    user_question: UserQuestionColor = Relationship(back_populates="user_q_datas")

class UserQDataColorCreate(UserQDataCreate[int]):
    value: int

# List of all UserQuestion Models:
userQuestionModels: list[type[UserQuestionBase]] = [UserQuestionColor]
userDataModels: list[type[UserQDataBaseTable]] = [UserQDataColor]