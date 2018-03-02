import rpyc

conn = rpyc.connect("localhost", 18861)
print(conn.root)

subobject = conn.root.get_sub_object()
print(type(subobject))
print(subobject.method1())