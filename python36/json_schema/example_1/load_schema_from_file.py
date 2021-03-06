import python_jsonschema_objects as pjs

builder = pjs.ObjectBuilder("person.schema.json")

ns = builder.build_classes()

# Classes built from the schema.  Note that the inner classes are anonymous.
# Look to explicitly define them in future examples.
print("\nClasses")
print(dir(ns))

# Access the Person Class
Person = ns.Person

# Construct A new person with the top level required fields.
james = Person(firstName="James", lastName="Bond")

# Fields can be access either as properties or through the dictionary interface.
print("\nSpecific Fields")
print(f"{james.firstName} {james.lastName}")
print(f"{james['firstName']}, {james['lastName']}")

# List the attributes of the class.
print("\nClass")
print(james)

# Note that the validation defined in the schema is enforced on the object.
print("\nValidation")
try:
    james.age = -2
except pjs.validators.ValidationError as e:
    print(e)

# JSON Serialize the object and its nested objects.
print("\nJSON serialization")
print(james.serialize(sort_keys=True))


# Assign to the nested address object.
james.address = {"street": "1 Palace Place", "city": "London"}
print("\nAddress")
print(james.serialize(sort_keys=True))

print("\nAddress Type")
print(type(james.address))

# Access the Address Class
Address = getattr(ns, "Address<anonymous>")
print(Address.__dict__)
address = Address(street="1 Palace Place", city="London")
james.address = address

# Serialize and access the objects nested properties in a natural properties syntax.
print("Person w/ address")
print(james.serialize(sort_keys=True))
print(james.address.street)
