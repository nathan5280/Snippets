# Examples for using type hinting in PyCharm
from typing import List
from python.type_hinting.classes import ChildClass, BaseClass


def hello_world(location):
    """
    :rtype: None
    :param location: Where you are located
    :type location: str
    """
    print('Hello, World from {location}'.format(location=location))


def hello_world_return(location):
    """
    :rtype: str
    :param location: Where you are located
    :type location: str
    """
    return 'Hello, World from {location}'.format(location=location)


def parameter_type():
    """
    Get warning for passing int instead of string to hello_world
    """
    hello_world(1)


def return_type():
    """
    Warning for assigning a return value from a function that has no return value.
    """
    junk = hello_world('1')
    print(junk)


def return_type_type():
    """
    Check that type hint of int doens't allow assignment of string.
    """
    x = 1  # type: int
    print(x)

    x = 'str'  # Would like to see a x is int but assigned value of string warning.
    print(x)

    x = hello_world_return('str')  # Would like to see a x is int but assigned value of string warning.
    print(x)


def variable_not_used():
    # Warning for variable assigned but not used.
    unused_variable = 1


def type_check_class(o):
    """
    :rtype: None
    :param o:
    :type o: ChildClass
    """
    o.announce()


def argument_class1():
    # Expect ChildClass passing string
    type_check_class('1')


def argument_class2():
    ob = BaseClass()
    # Expect ChildClass passing BaseClass
    type_check_class(ob)

    oc = ChildClass()
    # Expected ChildClass passing ChildClass
    type_check_class(oc)


def variable_type():
    li = []  # type: List[int]
    ls = []  # type: List[str]
    # Expected int but argument is string
    li.append('string')

    # Expected string but argument is int
    ls.append(1)
