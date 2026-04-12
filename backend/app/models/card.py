"""Card model."""

from enum import Enum

from sqlalchemy import Column, Text
from sqlmodel import Field, SQLModel


class CardType(str, Enum):
    """Card type enum."""

    CHARACTER = "CHARACTER"
    EVENT = "EVENT"
    STAGE = "STAGE"
    LEADER = "LEADER"


class CardBase(SQLModel):
    """CardBase."""

    card_id: str = Field(unique=True, description="Card number (e.g. OP01-001).")
    card_name_id: int = Field(
        foreign_key="card_names.id",
        description="Foreign key to CardName.",
    )
    card_type: CardType = Field(
        description="Card type (CHARACTER / EVENT / STAGE / LEADER).",
    )
    cost: int = Field(description="Cost.")
    power: int | None = Field(default=None, description="Power.")
    counter: int | None = Field(
        default=None,
        description="Counter value (1000 or 2000).",
    )
    block_icon_number: int = Field(
        ge=1,
        description="Block icon number (positive integer).",
    )
    is_comic_parallel: bool = Field(
        default=False,
        description="Whether the card is a comic parallel.",
    )
    rarity: str = Field(description="Rarity.")
    effect_text: str | None = Field(
        default=None,
        sa_column=Column(Text, nullable=True),
        description="Effect text.",
    )
    trigger_text: str | None = Field(
        default=None,
        sa_column=Column(Text, nullable=True),
        description="Trigger effect text.",
    )


class Card(CardBase, table=True):
    """Card."""

    __tablename__ = "cards"

    id: int | None = Field(default=None, primary_key=True, description="Primary key.")


class CardCreate(CardBase):
    """CardCreate."""


class CardRead(CardBase):
    """CardRead."""

    id: int = Field(description="Primary key.")
