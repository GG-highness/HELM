from sqlmodel import Field, SQLModel


class CardSetBase(SQLModel):
    code: str = Field(unique=True, description="弾コード（例: OP01, ST01）")
    name: str = Field(description="弾名（例: ROMANCE DAWN）")


class CardSet(CardSetBase, table=True):
    __tablename__ = "card_sets"

    id: int | None = Field(default=None, primary_key=True)


class CardSetCreate(CardSetBase):
    pass


class CardSetRead(CardSetBase):
    id: int
