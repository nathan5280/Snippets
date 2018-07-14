from types import SimpleNamespace
from collections import namedtuple

list_data = [
    [11, 12],
    [21, 22]
]

dict_data = [
    {"col1": 11, "col2": 12},
    {"col1": 21, "col2": 22}
]

# SimpleNamespace
ns = SimpleNamespace(col1=list_data[0][0],
                     col2=list_data[0][1])

print("SimpleNamespace")
print("__repr__")
print(ns)
print("dot access")
print("ns.col1: ", ns.col1)
print()

print("From kwargs")
ns = SimpleNamespace(**dict_data[0])
print("kwargs: ", ns)
print("ns.col1: ", ns.col1)

# Add attr
ns.col3 = 13
print(ns)

# Delete attr
del ns.col1
print(ns)

# Convert object to dict.
row_dict = vars(ns)
print("Dict: ", row_dict)

# NamedTuple
print()
print("NamedTuple")
RowClass = namedtuple("Row", ("col1", "col2"))
row = RowClass(11, 12)
print("positional, __repr__", row)
row = RowClass(col1=11, col2=12)
print("named, __repr__", row)

# Not as flexible as SimpleNamespace.  Unable to assign new attribute.
try:
    row.col3 = 12
except AttributeError:
    pass

rows = []
for data in dict_data:
    row = RowClass(**data)
    rows.append(row)

print(rows)