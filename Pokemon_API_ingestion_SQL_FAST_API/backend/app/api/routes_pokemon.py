from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.db.models import Pokemon, PokemonType, Type
from app.services.query_service import PokeQueryService

router = APIRouter(prefix="/pokemon", tags=["pokemon"])


class PokemonOut(BaseModel):
    id: int
    name: str
    types: List[str] = []  # default to empty list
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int
    tanky_label: str

    class Config:
        from_attributes = True


@router.get("/", response_model=List[PokemonOut])
def list_pokemon(
    type_filter: Optional[str] = Query(None, alias="type"),
    tanky: Optional[bool] = None,
    limit: int = 50,
    offset: int = 0,
    db: Session = Depends(get_db),
) -> List[PokemonOut]:
    """
    List Pokémon with optional filtering by type and tanky status.
    """
    qs = PokeQueryService(db)
    labels = {row["id"]: row["label"] for row in qs.tanky_labels()}

    stmt = select(Pokemon)

    if type_filter:
        stmt = (
            stmt.join(Pokemon.types)
            .join(PokemonType.type_)
            .where(Type.name == type_filter)
        )

    stmt = stmt.offset(offset).limit(limit)
    pokes = db.execute(stmt).scalars().all()

    result: List[PokemonOut] = []

    for p in pokes:
        # p.types is a relationship; coerce to empty list if None
        rel_types = p.types or []
        type_names = [pt.type_.name for pt in rel_types]
        tanky_label = labels.get(p.id, "not tanky")

        # apply tanky filter AFTER computing label
        if tanky is not None:
            if tanky and tanky_label != "tanky":
                continue
            if not tanky and tanky_label != "not tanky":
                continue

        result.append(
            PokemonOut(
                id=p.id,
                name=p.name,
                types=type_names,
                hp=p.hp,
                attack=p.attack,
                defense=p.defense,
                special_attack=p.special_attack,
                special_defense=p.special_defense,
                speed=p.speed,
                tanky_label=tanky_label,
            )
        )

    return result
