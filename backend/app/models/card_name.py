from sqlmodel import Field, SQLModel


class CardNameBase(SQLModel):
    name: str = Field(unique=True)


class CardName(CardNameBase, table=True):
    __tablename__ = "card_names"

    id: int | None = Field(default=None, primary_key=True)


class CardNameCreate(CardNameBase):
    pass


class CardNameRead(CardNameBase):
    id: int
