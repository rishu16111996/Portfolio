from config import db
from handleMetadata import parse_metadata_string

_current_schema = None
_current_class = None


def generate_model_class(class_name, fields):
    print("MODEL FIELDS:", fields)

    sqlalchemy_fields = {
        '__table_args__': {'extend_existing': True}
    }

    # Build SQLAlchemy columns
    for field_name, (field_type, params) in fields.items():

        if field_type.lower() == "string":
            col_type = db.String(params.get("length", 80))
        elif field_type.lower() == "integer":
            col_type = db.Integer
        else:
            raise ValueError(f"Unknown SQLAlchemy type: {field_type}")

        final_params = {k: v for k, v in params.items() if k != "length"}
        sqlalchemy_fields[field_name] = db.Column(col_type, **final_params)

    # Table name is dynamic
    sqlalchemy_fields["__tablename__"] = class_name.lower()

    # to_json
    def to_json(self):
        return {col: getattr(self, col) for col in self.__table__.columns.keys()}

    sqlalchemy_fields["to_json"] = to_json

    ModelClass = type(class_name, (db.Model,), sqlalchemy_fields)
    return ModelClass


def get_output(schema_str=None, class_name="DynamicModel"):

    global _current_schema, _current_class

    if schema_str:
        _current_schema = parse_metadata_string(schema_str)
        _current_class = class_name  # store model name

    if _current_schema is None:
        _current_schema = parse_metadata_string()

    if _current_class is None:
        _current_class = class_name

    return generate_model_class(_current_class, _current_schema)
