# JSON Conversion Tool

This JSON Conversion Tool is a Python library that allows you to convert JSON objects from one schema to another using a set of conversion rules. The library is designed to handle JSON objects of any complexity and supports simple data transformations during the conversion process.

## Features
* Convert JSON objects from one schema to another.
* Support for nested JSON objects.
* Apply simple data transformations during the conversion process.
* Store conversion rules in JSON format.

## Installation
You can simply clone this repository or copy the provided Python functions into your project.
```bash
git clone https://github.com/yourusername/json-conversion-tool.git
```

## Usage
Here's an example of how to use the JSON Conversion Tool:

```python
from json_conversion_tool import convert_json

source = {"id": 1, "name": "Alice", "age": "25"}

target_schema = {"userId": None, "fullName": None, "userAge": None}

conversion_rules = [
    {"source_key": "id", "target_key": "userId", "transformation": "int_to_str"},
    {"source_key": "name", "target_key": "fullName"},
    {"source_key": "age", "target_key": "userAge", "transformation": "str_to_int"},
]

converted_json = convert_json(source, json.dumps(target_schema), conversion_rules)
print(converted_json)
```

## Conversion Rules
The conversion rules are specified as a list of dictionaries with the following keys:

* `**source_key**`: The key in the source JSON object.
* `**target_key**`: The key in the target JSON object.
* `**transformation**` (optional): A simple data transformation to apply during the conversion process.

## Supported Transformations
* `**str_to_int**`: Convert a string to an integer.
* `**int_to_str**`: Convert an integer to a string.

You can add more transformations in the transform_data function as needed.

## Contributing

Pull requests are welcome 💗💡. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)