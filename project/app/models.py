from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
#
##
### BASEMODELS
##
#
class UserQuestionBase(SQLModel):
    question_text: str
    created_at: datetime = Field(default=datetime.now(), nullable=False)
    updated_at: datetime | None = Field(default=None)
    deleted_at: datetime | None = Field(default=None)

    #answer_set: list["UserQuestionAnswerSetLinkBase"]
    #user_datas: list["UserDataBase"]

    #question_type: str

class UserQuestionAnswerSetLinkBase(SQLModel):
    pass

class UserDataBase(SQLModel):
    value: str
    for_date: datetime | None = Field(default=datetime.now(), nullable=False)
    created_at: datetime = Field(default=datetime.now(), nullable=False)
    updated_at: datetime | None = Field(default=None)
    deleted_at: datetime | None = Field(default=None)

    #user_question: UserQuestionBase
#
##
### COLORS
##
#
class UserQuestionColorLink(UserQuestionAnswerSetLinkBase, table=True):
    user_question_id: int = Field(foreign_key="userquestioncolor.id", nullable=False, primary_key=True)
    color_id: int = Field(foreign_key="color.id", nullable=False, primary_key=True)
    
class Color(SQLModel, table=True):
    id: int | None = Field(default=None, nullable=False, primary_key=True)
    label: str | None
    color: str = Field(..., index=True, unique=True, regex=r'^#[0-9A-Fa-f]{6}$')
    created_at: datetime = Field(default=datetime.now(), nullable=False)
    deleted_at: datetime | None = Field(default=None)
    
    user_questions: list["UserQuestionColor"] = Relationship(back_populates="answer_set", link_model=UserQuestionColorLink)

class UserQuestionColor(UserQuestionBase, table=True):
    id: int | None = Field(default=None, nullable=False, primary_key=True)
    
    answer_set: list["Color"] = Relationship(back_populates="user_questions", link_model=UserQuestionColorLink)
    user_datas: list["UserDataColor"] = Relationship(back_populates="user_question")


class UserDataColor(UserDataBase, table=True):
    id: int | None = Field(default=None, nullable=False, primary_key=True)

    user_question_id: int = Field(foreign_key="userquestioncolor.id", nullable=False)
    user_question: UserQuestionColor = Relationship(back_populates="user_datas")


# List of all UserQuestion Models:
userQuestionModels: list[type[UserQuestionBase]] = [UserQuestionColor]