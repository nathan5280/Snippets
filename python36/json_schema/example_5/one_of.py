import python_jsonschema_objects as pjs

examples = {
    "Age": {
        "title": "Age",
        "type": "integer"
    },
    "Address": {
        "title": "Address",
        "type": "string"
    },
    "Other": {
        "title": "Other",
        "type": "object",
        "properties": {
            "MyAddress": {"$ref": "memory:Address"}
        },
        "additionalProperites": False
    },
    "Example Schema": {
        "title": "Example Schema",
        "type": "object",
        "properties": {
            "firstName": {
                "type": "string"
            },
            "lastName": {
                "type": "string"
            },
            "age": {
                "description": "Age in years",
                "type": "integer",
                "minimum": 0
            },
            "dogs": {
                "type": "array",
                "items": {"type": "string"},
                "maxItems": 4
            },
            "address": {
                "type": "object",
                "properties": {
                    "street": {"type": "string"},
                    "city": {"type": "string"},
                    "state": {"type": "string"}
                },
                "required": ["street", "city"]
            },
            "gender": {
                "type": "string",
                "enum": ["male", "female"]
            },
            "deceased": {
                "enum": ["yes", "no", 1, 0, "true", "false"]
            }
        },
        "required": ["firstName", "lastName"]
    },
    "OneOf": {
        "title": "OneOf",
        "type": "object",
        "properties": {
            "MyData": {
                "oneOf": [
                    {"$ref": "memory:Address"},
                    {"$ref": "memory:Age"}
                ]
            }
        },
        "additionalProperties": False
    },
    "OneOfBare": {
        "title": "OneOfBare",
        "type": "object",
        "oneOf": [
            {"$ref": "memory:Other"},
            {"$ref": "memory:Example Schema"}
        ],
        "additionalProperties": False
    }
}

builder = pjs.ObjectBuilder(examples["OneOf"], resolved=examples)
ns_one_of = builder.build_classes()

builder = pjs.ObjectBuilder(examples["OneOfBare"], resolved=examples)
ns_one_of_bare = builder.build_classes()

print(dir(ns_one_of))
print(dir(ns_one_of_bare))