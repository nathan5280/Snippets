"""
*arg and **kwarg are powerful ways to pass and consume function arguments.  Understanding how to use them
can save time and create flexibility in applications.

Function declaration:
    *args:
        - allows the function to except an unknown list of positional arguments.
    **kwargs:
        - allows the function to except an unknown list of named arguments.

Function call:
    *args:
        - Explodes a list of arguments into positional arguments in the function's arguments.
    **kwargs:
        - Exploes a dictionary of arguments into named arguments in the function's arguments.
"""
from typing import Dict, List


def positional_decl(a1: int, a2: int = 2) -> List[int]:
    """
    Simple positional or named argument declaration.
    """
    return [a1, a2]


def positional():
    """
    Different ways to call positional functions declarations.
    """
    print(f"\n{__file__}:positional")

    print("\tPositional:", positional_decl(1))
    print("\tNamed:", positional_decl(a2=3, a1=1))


def force_named_decl(*, a1: int, a2: int = 2) -> List[int]:
    """
    Force all arguments to be named.
    """
    return [a1, a2]


def force_named():
    """
    Different ways to call function that only accepts named arguments.
    """
    print(f"\n{__file__}:force_named")

    print("\tNamed:", force_named_decl(a1=1))

    # Unaccepted positional argument.
    try:
        force_named_decl(0, a1=1)
    except TypeError as e:
        print("\tPositional:", e)

    # Extra named argument.
    try:
        force_named_decl(a1=1, a3=3)
    except TypeError as e:
        print("\tExtra Named:", e)


def unknown_positional_decl(a1: int, *args: int) -> List[int]:
    """
    Declaration to accept one positional and an unknown number of additional positional arguments.
    """
    result = [a1]
    for arg in args:
        result.append(arg)

    return result


def unknown_positional():
    """
    Different ways to call variable number of positional arguments.
    """
    print(f"\n{__file__}:unknown_positional")

    print("\tVariable Positional:", unknown_positional_decl(1, 2, 3))

    input_list = [ 1, 2, 3]
    print("\tInput List:", unknown_positional_decl(*input_list))


def unknown_named_decl(*, a1: int, **kwargs: int) -> Dict[str, int]:
    """
     Declaration ot accept only named arguments.  One is required and any number of additional arguments are accepted.
    """
    result = dict()
    result["a1"] = a1
    result.update(kwargs)
    return result


def unknown_named():
    """
    Different ways to call variable number of named arguments.
    """
    print(f"\n{__file__}:unknown_named")

    print("\tNamed:", unknown_named_decl(a1=1, a2=2, a3=3))

    input_dict = {
        "a1": 1,
        "a2": 2,
        "a3": 3
    }

    print("\tInput Dictionary:", unknown_named_decl(**input_dict))


if __name__ == '__main__':
    positional()
    force_named()
    unknown_positional()
    unknown_named()
