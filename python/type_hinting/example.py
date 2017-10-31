# Examples for using type hinting in PyCharm
from typing import List
from python.type_hinting.classes import ChildClass, BaseClass


def hello_world(location: str) -> None:
    print('Hello, World from {location}'.format(location=location))


def hello_world_return(location: str) -> str:
    return 'Hello, World from {location}'.format(location=location)


def parameter_type():
    # Warning for int parameter passed when string expected.
    hello_world(1)


def return_type():
    # Warning for assigning a return value from a function that has no return value.
    junk = hello_world('1')
    print(junk)


def return_type_type():
    x = 1  # type: int
    print(x)

    x = hello_world_return('1')
    print(x)


def variable_not_used():
    # Warning for variable assigned but not used.
    unused_variable = 1


def type_check_class(o: ChildClass) -> None:
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
