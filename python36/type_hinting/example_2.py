# Examples for using type hinting in PyCharm
from typing import List
from python.type_hinting.classes import SubClassA, BaseClass


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


def variable_not_used():
    # Warning for variable assigned but not used.
    unused_variable = 1


def argument_class2():
    def type_check_sub_class(o: SubClassA) -> None:
        o.indexed_announce()

    def type_check_base_class(o: BaseClass) -> None:
        o.indexed_announce()

    obj = BaseClass(1)
    # Expect SubClassA passing BaseClass
    type_check_sub_class(obj)

    # Good
    type_check_base_class(obj)

    obj = SubClassA(2)
    # Good
    type_check_sub_class(obj)

    # Good
    type_check_base_class(obj)


def variable_type():
    li = []  # type: List[int]
    ls = []  # type: List[str]
    # Expected int but argument is string
    li.append('string')

    # Good
    li.append(1)

    # Expected string but argument is int
    ls.append(1)

    # Good
    ls.append('1')
