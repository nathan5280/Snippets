import python_jsonschema_objects as pjs

examples = {
    "Circular References": {
        "title": "Circular Refrence",
        "id": "foo",
        "type": "object",
        "oneOf": [
            {"$ref": "#/definitions/A"},
            {"$ref": "#/definitions/B"}
        ],
        "definitions": {
            "A": {
                "type": "object",
                "properties": {
                    "message": {"type": "string"},
                    "reference": {"$ref": "#/definitions/B"}
                },
                "required": ["message"]
            },
            "B": {
                "type": "object",
                "properties": {
                    "author": {"type": "string"},
                    "reference": {"$ref": "#/definitions/A"}
                },
                "required": ["author"]
            }
        }
    }
}

builder = pjs.ObjectBuilder(examples["Circular References"])
ns = builder.build_classes()

a = ns.A()
print("\nA")
for attr in dir(ns.A):
    print(attr)

print("\na.message")
print(a.message)
a.message = "foo"
print(a.message)

print("\nReference to B")
b = ns.B()
try:
    a.reference = b
except pjs.validators.ValidationError as e:
    print(e)

b.author = "Stephen King"
a.reference = b

print(a.serialize())
