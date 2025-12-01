from app.db.session import SessionLocal
from app.services.ingest_service import PokeIngestService


def main():
    db = SessionLocal()
    try:
        svc = PokeIngestService(db)
        svc.ingest_range()
        print("Ingested Pokémon 1–151.")
    finally:
        db.close()


if __name__ == "__main__":
    main()
