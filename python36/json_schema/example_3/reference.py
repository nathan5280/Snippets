import python_jsonschema_objects as pjs

examples = {
    "Address": {
        "title": "Address",
        "type": "string"
    },
    "Just a Reference": {
        "title": "Just a Reference",
        "$ref": "memory:Address"
    }
}

builder = pjs.ObjectBuilder(examples["Just a Reference"], resolved=examples)

ns = builder.build_classes()
print(ns.JustAReference('Hello'))


examples = {
    # "Address": {
    #     "title": "Address",
    #     "type": "string"
    # },
    "AddlPropsAllowed": {
        "title": "AddlPropsAllowed",
        "type": "object",
        "additionalProperties": True
    },
    "Other": {
        "title": "Other",
        "type": "object",
        "properties": {
            "MyAddress": {"$ref": "memory:Address"}
        },
        "additionalProperites": False
    }
}

builder = pjs.ObjectBuilder(examples['Other'], resolved={"Address": {"type": "string"}})
builder.validate({"MyAddress": "1234"})
ns = builder.build_classes()

print("\nClasses")
print(dir(ns))

thing = ns.Other()
print("\nthing")
print(thing)

# Address
thing.MyAddress = "Franklin Square"
print("\nAddress")
print(thing.serialize())

# Use Address defined in schema.
print("\n\nSchema defined address")
examples = {
    "Address": {
        "title": "Address",
        "type": "string"
    },
    "AddlPropsAllowed": {
        "title": "AddlPropsAllowed",
        "type": "object",
        "additionalProperties": True
    },
    "Other": {
        "title": "Other",
        "type": "object",
        "properties": {
            "MyAddress": {"$ref": "memory:Address"}
        },
        "additionalProperites": False
    }
}

builder = pjs.ObjectBuilder(examples['Other'], resolved=examples)
builder.validate({"MyAddress": "1234"})
ns = builder.build_classes()

print("\nClasses")
print(dir(ns))
