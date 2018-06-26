"""
Test case to show that the default argument is only evaluated when the file is
initially loaded.  All instances of the class get the same default argument object.

If this object is mutable then changes to the argement in one object impact all other
objects created with this default argement.
"""
from typing import List


class MutableDefaultArg:
    def __init__(self, mutable_arg: List[str] = []):
        self.arg = mutable_arg


def test_mutable_arg():
    # given

    # execute
    obj_1 = MutableDefaultArg()
    obj_2 = MutableDefaultArg()

    # expect
    assert obj_1.arg is obj_2.arg

    # execute
    obj_1.arg.append("a")

    # expect
    # This is the interesting side effect of all objects of type MutableDefaultArg constructed
    # using the default argument share the same list.
    assert obj_1.arg is obj_2.arg
    assert 1 == len(obj_1.arg)
    assert 1 == len(obj_2.arg)
    assert obj_1.arg[0] == obj_2.arg[0]


class NoneMutableDefaultArg:
    def __init__(self, mutable_arg: List[str] = None):
        self.arg = mutable_arg if mutable_arg else []


def test_none_mutable_arg():
    # given

    # execute
    obj_1 = NoneMutableDefaultArg()
    obj_2 = NoneMutableDefaultArg()

    # expect
    assert obj_1.arg is not obj_2.arg

    # execute
    obj_1.arg.append("a")

    # expect
    # This is the interesting side effect of all objects of type MutableDefaultArg constructed
    # using the default argument share the same list.
    assert obj_1.arg is not obj_2.arg
    assert 1 == len(obj_1.arg)
    assert 0 == len(obj_2.arg)
