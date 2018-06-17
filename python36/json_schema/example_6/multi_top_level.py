import python_jsonschema_objects as pjs

schema = {
    "title": "MultipleObjects",
    "id": "foo",
    "type": "object",
    "oneOf": [
        {"$ref": "#/definitions/ErrorResponse"},
        {"$ref": "#/definitions/VersionGetResponse"}
    ],
    "definitions": {
        "ErrorResponse": {
            "title": "Error Response",
            "id": "Error Response",
            "type": "object",
            "properties": {
                "message": {"type": "string"},
                "status": {"type": "integer"}
            },
            "required": ["message", "status"]
        },
        "VersionGetResponse": {
            "title": "Version Get Response",
            "type": "object",
            "properties": {
                "local": {"type": "boolean"},
                "version": {"type": "string"}
            },
            "required": ["version"]
        }
    }
}


builder = pjs.ObjectBuilder(schema)

ns = builder.build_classes()

print("\nns")
for attr in dir(ns):
    print("\t", attr)

print("\nErrorResponse")
for attr in vars(ns.ErrorResponse):
    print("\t", attr)

print("\nVersionGetResponse")
for attr in vars(ns.VersionGetResponse):
    print("\t", attr)