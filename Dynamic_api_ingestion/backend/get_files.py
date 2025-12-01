import requests
from config import db
from models import get_output
import os

def if_file_exist():
    db.session.remove()
    db.engine.dispose()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "instance", "mydatabase.db")

    instance_dir = os.path.join(base_dir, "instance")
    os.makedirs(instance_dir, exist_ok=True)
    os.chmod(instance_dir, 0o777)

    if os.path.exists(file_path):
        os.chmod(file_path, 0o666)
        os.remove(file_path)


def connect_to_server(dummy_limit, url_passed):
    """
    Generic ingestion function for ANY API.
    Special-cases PokeAPI list endpoint to fetch full Pokémon details.
    """

    if_file_exist()
    db.create_all()

    Model = get_output()

    print("API URL:", url_passed)
    resp = requests.get(url_passed)
    resp.raise_for_status()
    response = resp.json()

    items = []

    if "pokeapi.co/api/v2/pokemon" in url_passed:
        # PokeAPI returns {"results": [...]}
        if isinstance(response, dict) and "results" in response:
            base_items = response["results"]
        elif isinstance(response, list):
            base_items = response
        else:
            base_items = []

        print(f"Pokemon base items: {len(base_items)}")

        for base in base_items:
            detail_url = base.get("url")
            if not detail_url:
                detail_url = url_passed.rstrip("/") + f"/{base.get('name')}"

            detail_resp = requests.get(detail_url)
            detail_resp.raise_for_status()
            detail = detail_resp.json()

            # Extract stats + types
            stats = {s["stat"]["name"]: s["base_stat"] for s in detail.get("stats", [])}
            types = [t["type"]["name"] for t in detail.get("types", [])]

            row = {
                "id": detail.get("id"),
                "name": detail.get("name"),
                "type1": types[0] if len(types) > 0 else None,
                "type2": types[1] if len(types) > 1 else None,
                "hp": stats.get("hp"),
                "attack": stats.get("attack"),
                "defense": stats.get("defense"),
                "special_attack": stats.get("special-attack"),
                "special_defense": stats.get("special-defense"),
                "speed": stats.get("speed"),
            }

            items.append(row)

    else:
        if isinstance(response, dict) and "results" in response:
            items = response["results"]
        else:
            items = response

    if not isinstance(items, list):
        items = [items]

    print("MODEL FIELDS:", {k: v for k, v in Model.__dict__.items() if not k.startswith("_")})

    # Insert rows
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            continue

        if "id" not in item:
            item["id"] = index + 1

        new_row = Model()

        for col in Model.__table__.columns.keys():
            if col in item:
                value = item[col]
            else:
                value = item.get(col.lower()) or item.get(col.upper()) or None

            col_type = str(Model.__table__.columns[col].type)
            if "INTEGER" in col_type.upper() and value is not None:
                try:
                    value = int(value)
                except Exception:
                    value = None

            setattr(new_row, col, value)

        db.session.add(new_row)

    db.session.commit()

    return f"{len(items)} records added"
