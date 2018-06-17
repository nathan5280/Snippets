# JSON Schema Defined Python Objects

**Reference Documentation
```http request
https://python-jsonschema-objects.readthedocs.io/en/latest/
```

There isn't a lot of new material here that isn't in the documentation, but it took a bit of interpreting
to get the first couple of examples running.  Hopefully having the examples here helps speed up the 
learning curve.

I was exploring the python bindings between JSON, JSON Schema and Python Objects to see about better documentation
and a more natural implementation of Flask, Python Model Objects, and DB.   

Thoughts: 
* JSON Schema seems like a reasonable good way to document the data portions of HTTP interactions.  It may
turn out that something like RMAL will turn out ot be a more complete solution for this.

* Mapping between JSON and Python Objects using JSON Schema and python_jsonschema_object may be useful
when complex JSON is used to define configuration information for an application.   I'm not happy with
having complext dictionaries that get passed around and the only way to see what goes in the configuration file
is to look to see what keys are accessed in the code.  Also the tedious nature of building classes to validate
and check all the configuration isn't really sustainable.  Using the schema to validate the JSON and build the 
classes seems like a good solution for this.