from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

class QuestionType(SQLModel, table=True):
    id: int | None = Field(default=None, nullable=False, primary_key=True)
    label: str
    tech_id: str = Field(index=True, unique=True)
    created_at: datetime = Field(default=datetime.now(), nullable=False)
    deleted_at: datetime | None = Field(default=None)

    user_questions: list["UserQuestion"] = Relationship(back_populates="question_type")

class Color(SQLModel, table=True):
    id: int | None = Field(default=None, nullable=False, primary_key=True)
    label: str | None
    color: str = Field(..., index=True, unique=True, regex=r'^#[0-9A-Fa-f]{6}$')
    created_at: datetime = Field(default=datetime.now(), nullable=False)
    deleted_at: datetime | None = Field(default=None)

    user_question_answerset_colors: list["UserQuestionAnswersetColor"] = Relationship(back_populates="color")

class UserQuestion(SQLModel, table=True):
    id: int | None = Field(default=None, nullable=False, primary_key=True)
    question_text: str
    created_at: datetime = Field(default=datetime.now(), nullable=False)
    updated_at: datetime | None = Field(default=None)
    deleted_at: datetime | None = Field(default=None)

    # foreign keys
    question_type_id: str = Field(foreign_key="questiontype.tech_id", nullable=False)
    question_type: QuestionType = Relationship(back_populates="user_questions")

    # many relations 
    user_question_answerset_colors: list["UserQuestionAnswersetColor"] = Relationship(back_populates="user_question")
    user_data_colors: list["UserDataColor"] = Relationship(back_populates="user_question")

class UserQuestionAnswersetColor(SQLModel, table=True):
    id: int | None = Field(default=None, nullable=False, primary_key=True)

    user_question_id: int = Field(foreign_key="userquestion.id", nullable=False)
    user_question: UserQuestion = Relationship(back_populates="user_question_answerset_colors")
    color_id: int = Field(foreign_key="color.id", nullable=False)
    color: Color = Relationship(back_populates="user_question_answerset_colors")

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