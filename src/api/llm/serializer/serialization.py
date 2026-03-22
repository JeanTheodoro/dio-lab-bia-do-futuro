import json
from decimal import Decimal
from datetime import date, datetime
from sqlalchemy.engine import RowMapping


def serialize_to_json(data):
    """
    Função genérica que converte:
    - RowMapping
    - Lista de RowMapping
    - Objetos ORM
    - Decimal
    - datetime/date
    """

    def serialize(obj):

        if isinstance(obj, list):
            return [serialize(item) for item in obj]

        if isinstance(obj, RowMapping):
            return {key: serialize(value) for key, value in dict(obj).items()}

        if hasattr(obj, "__dict__"):
            return {
                key: serialize(value)
                for key, value in obj.__dict__.items()
                if not key.startswith("_")
            }

        if isinstance(obj, Decimal):
            return float(obj)

        if isinstance(obj, (datetime, date)):
            return obj.isoformat()

        return obj

    serialized = serialize(data)
    return json.dumps(serialized, indent=2, ensure_ascii=False)