from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.session import Base


class Pokemon(Base):
    __tablename__ = "pokemon"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    hp: Mapped[int] = mapped_column(Integer, nullable=False)
    attack: Mapped[int] = mapped_column(Integer, nullable=False)
    defense: Mapped[int] = mapped_column(Integer, nullable=False)
    special_attack: Mapped[int] = mapped_column(Integer, nullable=False)
    special_defense: Mapped[int] = mapped_column(Integer, nullable=False)
    speed: Mapped[int] = mapped_column(Integer, nullable=False)

    types: Mapped[list["PokemonType"]] = relationship(
        "PokemonType", back_populates="pokemon", cascade="all, delete-orphan"
    )


class Type(Base):
    __tablename__ = "type"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    pokemon_types: Mapped[list["PokemonType"]] = relationship(
        "PokemonType", back_populates="type_", cascade="all, delete-orphan"
    )


class PokemonType(Base):
    __tablename__ = "pokemon_type"

    pokemon_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("pokemon.id", ondelete="CASCADE"), primary_key=True
    )
    type_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("type.id", ondelete="CASCADE"), primary_key=True
    )
    slot: Mapped[int] = mapped_column(Integer, nullable=False)

    pokemon: Mapped[Pokemon] = relationship("Pokemon", back_populates="types")
    type_: Mapped[Type] = relationship("Type", back_populates="pokemon_types")
