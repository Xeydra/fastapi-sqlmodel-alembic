from sqlmodel import SQLModel, Field


class InputTypeBase(SQLModel):
    id: str
    label: str
    techId: str

class InputType(InputTypeBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)


class InputTypeCreate(InputTypeBase):
    pass