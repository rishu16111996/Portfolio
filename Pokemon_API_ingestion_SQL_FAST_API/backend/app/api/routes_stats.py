from typing import List, Dict, Any, Tuple

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.query_service import PokeQueryService

router = APIRouter(prefix="/stats", tags=["stats"])


class TypeComboOut(BaseModel):
    type_combo: str
    count: int


class TankyTypeOut(BaseModel):
    type_name: str
    tanky_count: int


class RankingOut(BaseModel):
    type_name: str
    pokemon_name: str
    total_stats: int
    rank_in_type: int


class TankyLabelOut(BaseModel):
    id: int
    name: str
    label: str


@router.get("/type-combos", response_model=List[TypeComboOut])
def get_type_combos(db: Session = Depends(get_db)):
    qs = PokeQueryService(db)
    data: List[Tuple[str, int]] = qs.type_combo_counts()
    return [{"type_combo": combo, "count": cnt} for combo, cnt in data]


@router.get("/tanky-types", response_model=List[TankyTypeOut])
def get_tanky_types(db: Session = Depends(get_db)):
    qs = PokeQueryService(db)
    data = qs.types_with_most_tanky()
    return [{"type_name": t, "tanky_count": c} for t, c in data]


@router.get("/rankings", response_model=List[RankingOut])
def get_rankings(db: Session = Depends(get_db)):
    qs = PokeQueryService(db)
    data: List[Dict[str, Any]] = qs.rankings_per_type()
    return data


@router.get("/tanky-labels", response_model=List[TankyLabelOut])
def get_tanky_labels(db: Session = Depends(get_db)):
    qs = PokeQueryService(db)
    data = qs.tanky_labels()
    return data
