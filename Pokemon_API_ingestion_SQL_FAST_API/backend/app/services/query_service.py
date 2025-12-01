from typing import List, Tuple, Dict, Any
from sqlalchemy import text
from sqlalchemy.orm import Session


class PokeQueryService:
    def __init__(self, db: Session):
        self.db = db

    # ---------------------------------------------------------
    # Q1: Distinct type combination counts
    # ---------------------------------------------------------
    def type_combo_counts(self) -> List[Tuple[str, int]]:
        sql = text(
            """
            WITH typed AS (
                SELECT p.id AS pokemon_id,
                       group_concat(t.name, '/' ORDER BY pt.slot) AS type_combo
                FROM pokemon p
                JOIN pokemon_type pt ON p.id = pt.pokemon_id
                JOIN type t ON t.id = pt.type_id
                GROUP BY p.id
            )
            SELECT type_combo, COUNT(*) AS cnt
            FROM typed
            GROUP BY type_combo
            ORDER BY cnt DESC, type_combo;
            """
        )
        return [(r.type_combo, r.cnt) for r in self.db.execute(sql).all()]

    # ---------------------------------------------------------
    # Q3: Tanky labels (hp or defense = highest stat)
    # ---------------------------------------------------------
    def tanky_labels(self) -> List[Dict[str, Any]]:
        sql = text(
            """
            WITH max_stat AS (
                SELECT
                    id,
                    name,
                    hp,
                    attack,
                    defense,
                    special_attack,
                    special_defense,
                    speed,
                    (
                        SELECT MAX(x) FROM (
                            SELECT hp AS x
                            UNION ALL SELECT attack
                            UNION ALL SELECT defense
                            UNION ALL SELECT special_attack
                            UNION ALL SELECT special_defense
                            UNION ALL SELECT speed
                        )
                    ) AS max_val
                FROM pokemon
            )
            SELECT
                id,
                name,
                CASE
                    WHEN hp = max_val OR defense = max_val THEN 'tanky'
                    ELSE 'not tanky'
                END AS label
            FROM max_stat
            ORDER BY name;
            """
        )
        return [dict(row) for row in self.db.execute(sql).mappings().all()]

    # ---------------------------------------------------------
    # Q4: Which type(s) have the most tanky Pokémon?
    # ---------------------------------------------------------
    def types_with_most_tanky(self) -> List[Tuple[str, int]]:
        sql = text(
            """
            WITH max_stat AS (
                SELECT
                    id,
                    name,
                    hp,
                    attack,
                    defense,
                    special_attack,
                    special_defense,
                    speed,
                    (
                        SELECT MAX(x) FROM (
                            SELECT hp AS x
                            UNION ALL SELECT attack
                            UNION ALL SELECT defense
                            UNION ALL SELECT special_attack
                            UNION ALL SELECT special_defense
                            UNION ALL SELECT speed
                        )
                    ) AS max_val
                FROM pokemon
            ),
            labeled AS (
                SELECT
                    id,
                    CASE
                        WHEN hp = max_val OR defense = max_val THEN 1
                        ELSE 0
                    END AS is_tanky
                FROM max_stat
            ),
            per_type AS (
                SELECT
                    t.name AS type_name,
                    COUNT(*) AS tanky_count
                FROM labeled l
                JOIN pokemon_type pt ON l.id = pt.pokemon_id
                JOIN type t ON t.id = pt.type_id
                WHERE l.is_tanky = 1
                GROUP BY t.name
            ),
            max_counts AS (
                SELECT MAX(tanky_count) AS max_cnt FROM per_type
            )
            SELECT
                p.type_name,
                p.tanky_count
            FROM per_type p, max_counts m
            WHERE p.tanky_count = m.max_cnt
            ORDER BY p.type_name;
            """
        )
        return [(r.type_name, r.tanky_count) for r in self.db.execute(sql).all()]

    # ---------------------------------------------------------
    # Q2: Rank Pokémon by total stats per type
    # ---------------------------------------------------------
    def rankings_per_type(self) -> List[Dict[str, Any]]:
        sql = text(
            """
            WITH totals AS (
                SELECT
                    p.id,
                    p.name,
                    (p.hp + p.attack + p.defense +
                     p.special_attack + p.special_defense + p.speed) AS total
                FROM pokemon p
            )
            SELECT
                t.name AS type_name,
                p.name AS pokemon_name,
                totals.total AS total_stats,
                RANK() OVER (
                    PARTITION BY t.name
                    ORDER BY totals.total DESC
                ) AS rank_in_type
            FROM totals
            JOIN pokemon p ON p.id = totals.id
            JOIN pokemon_type pt ON p.id = pt.pokemon_id
            JOIN type t ON t.id = pt.type_id
            ORDER BY t.name, rank_in_type, p.name;
            """
        )
        return [dict(row) for row in self.db.execute(sql).mappings().all()]
