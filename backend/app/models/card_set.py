"""CardSet model."""

from sqlmodel import Field, SQLModel


class CardSetBase(SQLModel):
    """CardSetBase."""

    code: str = Field(unique=True, description="Set code (e.g. OP01, ST01).")
    name: str = Field(description="Set name (e.g. ROMANCE DAWN).")


class CardSet(CardSetBase, table=True):
    """CardSet."""

    __tablename__ = "card_sets"

    id: int | None = Field(default=None, primary_key=True, description="Primary key.")


class CardSetCreate(CardSetBase):
    """CardSetCreate."""


class CardSetRead(CardSetBase):
    """CardSetRead."""

    id: int = Field(description="Primary key.")
