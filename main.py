import json
from typing import Any

def transform_data(data: Any, transformation: str) -> Any:
    """
    Apply a transformation to the given data.

    Args:
    - `data` (Any): The data to be transformed.
    - `transformation` (str): The transformation to be applied. Supported transformations: 'str_to_int', 'int_to_str'.
    
    Return
    - `Any` - Transformed data.
    """
    if transformation == "str_to_int":
        return int(data)
    elif transformation == "int_to_str":
        return str(data)
    # Add more transformations
    else:
        return data

def apply_conversion_rules(source_json, target_json, rules, current_key=None):
    """
    Apply the conversion rules to the source JSON and modify the target JSON accordingly.

    Args:
    - `source_json` (dict): The source JSON object.
    - `target_json` (dict): The target JSON object.
    - `rules` (list of dict): The list of conversion rules.
    - `current_key` (str, optional): The current key being processed (used for recursive calls). Defaults to None.
    """
    for rule in rules:
        source_key = rule["source_key"]
        target_key = rule["target_key"]
        transformation = rule.get("transformation", None)

        if current_key is not None:
            source_key = f"{current_key}.{source_key}"
            target_key = f"{current_key}.{target_key}"

        source_keys = source_key.split(".")
        target_keys = target_key.split(".")

        src_value = source_json
        try:
            for key in source_keys:
                src_value = src_value[key]
        except KeyError:
            continue

        if transformation:
            src_value = transform_data(src_value, transformation)

        target_container = target_json
        for key in target_keys[:-1]:
            if key not in target_container:
                target_container[key] = {}
            target_container = target_container[key]

        target_container[target_keys[-1]] = src_value


def convert_json(source_json, target_json_schema, rules):
    """
    Convert the source JSON object to the target JSON schema using the given conversion rules.

    Args:
    - `source_json` (dict): The source JSON object.
    - `target_json_schema` (str): The JSON schema string for the target JSON object.
    - `rules` (list of dict): The list of conversion rules.

    Return
    - `dict` - The converted JSON object.
    """
    target_json = json.loads(target_json_schema)
    apply_conversion_rules(source_json, target_json, rules)
    return target_json


if __name__ == "__main__":
    # Пример использования функции
    source = {"id": 1, "name": "Alice", "age": "25"}

    target_schema = {"userId": None, "fullName": None, "userAge": None}

    conversion_rules = [
        {"source_key": "id", "target_key": "userId", "transformation": "int_to_str"},
        {"source_key": "name", "target_key": "fullName"},
        {"source_key": "age", "target_key": "userAge", "transformation": "str_to_int"},
    ]

    converted_json = convert_json(source, json.dumps(target_schema), conversion_rules)
    print(converted_json)