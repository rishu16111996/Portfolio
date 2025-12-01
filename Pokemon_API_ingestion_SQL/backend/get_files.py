import requests
from models import Pokemon
from config import db
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
    else:
        pass

def connect_to_server(num_of_pokemon: int, url_passed=f"https://pokeapi.co/api/v2/pokemon/"):
    if_file_exist()
    db.create_all() 
    added = []
    for num in range(1, num_of_pokemon + 1):
        url = f"{url_passed}{num}"
        response = requests.get(url)
        data = response.json()

        name = data['name'] 
        types = [i["type"]["name"] for i in data["types"]]
        stats = {s['stat']['name']: s['base_stat'] for s in data['stats']}

        new_pokemon = Pokemon(
            name=name,
            type1=types[0],
            type2=types[1] if len(types) > 1 else None,
            hp=stats["hp"],
            attack=stats["attack"],
            defense=stats["defense"],
            special_attack=stats["special-attack"],
            special_defense=stats["special-defense"],
            speed=stats["speed"]
        )
        
        try:
            db.session.add(new_pokemon)
            db.session.commit()
        except Exception as e:
            return f"error {e}"
        
        added.append(f"{name}\n")

    return f"{len(added)} Pokemons added"
