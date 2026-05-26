import json
from jsonschema import validate

# 1. Open the file and load the JSON content
with open('test/schema.json', 'r') as f:
    schema = json.load(f)

# 1. Open the file and load the JSON content
with open('test/bad_example.json', 'r') as f:
    instance = json.load(f)
validate(instance=instance, schema=schema)