import time
from typing import Dict, Any, Iterable

import requests
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import Pokemon, Type, PokemonType

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/pokemon"
GEN1_RANGE = range(1, 152)

STAT_MAP = {
    "hp": "hp",
    "attack": "attack",
    "defense": "defense",
    "special-attack": "special_attack",
    "special-defense": "special_defense",
    "speed": "speed",
}


class PokeIngestService:
    def __init__(self, db: Session, base_url: str = POKEAPI_BASE_URL):
        self.db = db
        self.base_url = base_url

    def fetch_pokemon(self, pokemon_id: int) -> Dict[str, Any]:
        resp = requests.get(f"{self.base_url}/{pokemon_id}", timeout=10)
        resp.raise_for_status()
        return resp.json()

    def _get_or_create_type(self, name: str) -> Type:
        stmt = select(Type).where(Type.name == name)
        existing = self.db.execute(stmt).scalar_one_or_none()
        if existing:
            return existing
        t = Type(name=name)
        self.db.add(t)
        self.db.flush()
        return t

    def parse_pokemon_payload(self, payload: Dict[str, Any]) -> Pokemon:
        stats_raw = payload["stats"]
        stat_values = {}
        for s in stats_raw:
            stat_name = s["stat"]["name"]
            if stat_name not in STAT_MAP:
                continue
            mapped = STAT_MAP[stat_name]
            stat_values[mapped] = s["base_stat"]
        for k in STAT_MAP.values():
            stat_values.setdefault(k, 0)
        return Pokemon(
            id=payload["id"],
            name=payload["name"],
            hp=stat_values["hp"],
            attack=stat_values["attack"],
            defense=stat_values["defense"],
            special_attack=stat_values["special_attack"],
            special_defense=stat_values["special_defense"],
            speed=stat_values["speed"],
        )

    def ingest_range(self, ids: Iterable[int] = GEN1_RANGE, delay: float = 0.1) -> None:
        for pokemon_id in ids:
            payload = self.fetch_pokemon(pokemon_id)
            pokemon = self.parse_pokemon_payload(payload)

            type_rows = []
            for t in payload["types"]:
                type_name = t["type"]["name"]
                slot = t["slot"]
                type_obj = self._get_or_create_type(type_name)
                type_rows.append(
                    PokemonType(
                        pokemon_id=pokemon.id,
                        type_id=type_obj.id,
                        slot=slot,
                    )
                )

            existing = self.db.get(Pokemon, pokemon.id)
            if existing:
                self.db.delete(existing)
                self.db.flush()

            self.db.add(pokemon)
            for pt in type_rows:
                self.db.add(pt)

            self.db.commit()
            time.sleep(delay)
