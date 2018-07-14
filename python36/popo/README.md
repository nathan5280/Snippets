# Plain Old Python Objects (POPO)
POPO are dynamically created classes and object that only have attributes and no behaviour.

## types.SimpleNamespace
Creates a attribute only object based on the names of the arguments.   Attributes can be added and removed.

## collections.namedtuple
Creates a class with the attributes specified in the call to namedtuple.  Attributes are fixed.

## argsparse.namespace
This is a SimpleNamespace returned by argsparse.

## Converting to dictionary
Any of these arguments can be converted to a standard dictionary object with the vars function.
```python
dict_obj = vars(namespace_obj)
```

# Uses
Namespace and namedtuple objects a useful for converting from subscript notation to dotted notation for 
accessing data elements.  If you read data from a csv file you wind up with a row of data that is either that is
accessed using the [] subscript notation.  This will either be column index 0, 1, 2, ... or if there was 
a header row by the column name 'col1', 'col2', ...  This can be a bit of a pain to understand as the 
column index provides no information about what is in the column and the named index can be a pain if the
column names are long ('Engine Displacement in cm^3')

Both the SimpleNamespace and namedtuple transform the row data into a simpler form for accessing the data
and conveying information about the column data's meaning.

ns.eng_disp_cm3
