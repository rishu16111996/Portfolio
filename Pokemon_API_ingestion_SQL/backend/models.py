from config import db

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    type1 = db.Column(db.String(80), unique=False, nullable=False)
    type2 = db.Column(db.String(80), unique=False, nullable=True)
    hp = db.Column(db.Integer, unique=False, nullable=False)
    attack = db.Column(db.Integer, unique=False, nullable=False)
    defense = db.Column(db.Integer, unique=False, nullable=False)
    special_attack = db.Column(db.Integer, unique=False, nullable=False)
    special_defense = db.Column(db.Integer, unique=False, nullable=False)
    speed = db.Column(db.Integer, unique=False, nullable=False)
    

    def to_json(self):
        return{
            "id": self.id,
            "name": self.name,
            "type1": self.type1,
            "type2": self.type2,
            "hp": self.hp,
            "attack": self.attack,
            "defense": self.defense,
            "specialAttack": self.special_attack,
            "specialDefense": self.special_defense,
            "speed": self.speed,
        }
    