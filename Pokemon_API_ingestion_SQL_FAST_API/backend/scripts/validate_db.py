from app.db.session import SessionLocal
from app.db.models import Pokemon, PokemonType


def main():
    db = SessionLocal()
    try:
        # Find Pokémon that have no associated types
        missing_type_rows = (
            db.query(Pokemon)
            .outerjoin(PokemonType, Pokemon.id == PokemonType.pokemon_id)
            .filter(PokemonType.pokemon_id.is_(None))
            .all()
        )

        if not missing_type_rows:
            print("✅ All Pokémon have at least one type mapping.")
        else:
            print("⚠ Pokémon without types found:")
            for p in missing_type_rows:
                print(f" - id={p.id}, name={p.name}")
            print(
                "\nYou can fix this by recreating the DB and re-running ingestion:\n"
                "  rm pokemon.db\n"
                "  python scripts/create_db.py\n"
                "  python scripts/ingest_data.py\n"
            )

    finally:
        db.close()


if __name__ == "__main__":
    main()
