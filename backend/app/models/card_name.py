"""CardName model."""

from sqlmodel import Field, SQLModel


class CardNameBase(SQLModel):
    """CardNameBase."""

    name: str = Field(unique=True, description="Card name.")


class CardName(CardNameBase, table=True):
    """CardName."""

    __tablename__ = "card_names"

    id: int | None = Field(default=None, primary_key=True, description="Primary key.")


class CardNameCreate(CardNameBase):
    """CardNameCreate."""


class CardNameRead(CardNameBase):
    """CardNameRead."""

    id: int = Field(description="Primary key.")
