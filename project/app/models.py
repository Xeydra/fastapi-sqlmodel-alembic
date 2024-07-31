from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime


class InputType(SQLModel, table=True):
    id: int | None = Field(default=None, nullable=False, primary_key=True)
    label: str
    tech_id: str = Field(index=True, unique=True)
    created_at: datetime = Field(default=datetime.now(), nullable=False)
    deleted_at: datetime | None = Field(default=None)

    user_questions: list["UserQuestion"] = Relationship(back_populates="input_type")


class UserQuestion(SQLModel, table=True):
    id: int | None = Field(default=None, nullable=False, primary_key=True)
    question_text: str
    created_at: datetime = Field(default=datetime.now(), nullable=False)
    updated_at: datetime | None = Field(default=None)
    deleted_at: datetime | None = Field(default=None)

    input_type_id: str = Field(foreign_key="inputtype.tech_id", nullable=False)
    input_type: InputType = Relationship(back_populates="user_questions")

    user_data_colors: list["UserDataColor"] = Relationship(back_populates="user_question")


class UserDataColorBase(SQLModel):
    value: str
    for_date: datetime | None = Field(default=datetime.now(), nullable=False)
    user_question_id: int = Field(foreign_key="userquestion.id", nullable=False)

class UserDataColor(UserDataColorBase, table=True):
    id: int | None = Field(default=None, nullable=False, primary_key=True)
    created_at: datetime = Field(default=datetime.now(), nullable=False)
    updated_at: datetime | None = Field(default=None)
    deleted_at: datetime | None = Field(default=None)

    user_question_id: int = Field(foreign_key="userquestion.id", nullable=False)
    user_question: UserQuestion = Relationship(back_populates="user_data_colors")

class UserDataColorCreate(UserDataColorBase):
    pass