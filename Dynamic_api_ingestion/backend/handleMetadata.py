DEFAULT_POKEMON_SCHEMA = """
id: int primary_key,
name: string unique,
type1: string,
type2: string nullable,
hp: int,
attack: int,
defense: int,
special_attack: int,
special_defense: int,
speed: int
"""


def parse_metadata_string(schema_str=DEFAULT_POKEMON_SCHEMA):
    columns = [c.strip() for c in schema_str.split(",") if c.strip()]
    result = {}

    for col in columns:
        parts = [p.strip() for p in col.split() if p.strip()]
        if len(parts) < 2:
            raise ValueError(f"Invalid column definition: {col}")

        name_part = parts[0]
        col_name = name_part.replace(":", "")

        col_type = parts[1].lower()
        if col_type == "int":
            sql_type = "Integer"
        elif col_type == "string":
            sql_type = "String"
        else:
            raise ValueError(f"Unknown type: {col_type}")

        params = {"nullable": False}

        flags = parts[2:]
        for flag in flags:
            if flag == "primary_key":
                params["primary_key"] = True
            if flag == "unique":
                params["unique"] = True
            if flag == "nullable":
                params["nullable"] = True

        if sql_type == "String" and "length" not in params:
            params["length"] = 80

        result[col_name] = (sql_type, params)

    return result