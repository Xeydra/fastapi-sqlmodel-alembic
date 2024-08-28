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

class UserQuestionAnswerSetLinkBase(SQLModel):
    pass

class UserDataBase(SQLModel):
    value: str
    for_date: datetime | None = Field(default=datetime.now(), nullable=False)
    created_at: datetime = Field(default=datetime.now(), nullable=False)
    updated_at: datetime | None = Field(default=None)
    deleted_at: datetime | None = Field(default=None)

#
##
### COLORS
##
#
class UserQuestionColorLink(UserQuestionAnswerSetLinkBase, table=True):
    user_question_id: int = Field(foreign_key="userquestioncolor.id", nullable=False, primary_key=True)
    color_id: int = Field(foreign_key="color.id", nullable=False, primary_key=True)

class ColorBase(SQLModel):
    label: str | None
    color: str = Field(..., index=True, unique=True, regex=r'^#[0-9A-Fa-f]{6}$')

class Color(ColorBase, table=True):
    id: int | None = Field(default=None, nullable=False, primary_key=True)
    created_at: datetime = Field(default=datetime.now(), nullable=False)
    deleted_at: datetime | None = Field(default=None)
    
    user_questions: list["UserQuestionColor"] = Relationship(back_populates="answer_set", link_model=UserQuestionColorLink)

class ColorRead(ColorBase):
    pass

class UserQuestionColor(UserQuestionBase, table=True):
    id: int | None = Field(default=None, nullable=False, primary_key=True)
    
    answer_set: list["Color"] = Relationship(back_populates="user_questions", link_model=UserQuestionColorLink)
    user_datas: list["UserDataColor"] = Relationship(back_populates="user_question")

class UserQuestionColorRead(UserQuestionBase):
    answer_set: list["ColorRead"]
    user_datas: list["UserDataColor"]

class UserDataColor(UserDataBase, table=True):
    id: int | None = Field(default=None, nullable=False, primary_key=True)

    user_question_id: int = Field(foreign_key="userquestioncolor.id", nullable=False)
    user_question: UserQuestionColor = Relationship(back_populates="user_datas")


# List of all UserQuestion Models:
userQuestionModels: list[type[UserQuestionBase]] = [UserQuestionColor]
userDataModels: list[type[UserDataBase]] = [UserDataColor]