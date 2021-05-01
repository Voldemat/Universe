import json
from typing import Optional

def get_db_table_name(model:object) -> str:
    return model.objects.model._meta.db_table


def str_to_json(string:str) -> Optional[dict]:
    if not string:
        return None

    string = string.replace("\'",'\"')

    string = string.replace("None", "null")

    result = json.loads(string)

    return result