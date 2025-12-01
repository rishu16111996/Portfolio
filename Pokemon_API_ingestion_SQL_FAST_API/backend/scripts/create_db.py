from app.db.session import engine, Base
from app.db import models  # noqa: F401


def main():
    Base.metadata.create_all(bind=engine)
    print("Database tables created.")


if __name__ == "__main__":
    main()
