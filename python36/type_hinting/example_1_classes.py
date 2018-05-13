from python36.type_hinting.classes import BaseClass, SubClassA


def announce(obj: BaseClass, msg: str) -> str:
    return obj.indexed_announce(msg)


def direct_object() -> None:
    print(f"\n{__file__}:direct_object")

    a = SubClassA(1)

    print("\tString Message:", a.indexed_announce("Hello"))
    print("\tNo Message:", a.indexed_announce())


def passed_object() -> None:
    print(f"\n{__file__}:passed_object")

    a = SubClassA(2)

    print("\tString Message:", announce(a, "World"))


if __name__ == '__main__':
    direct_object()
    passed_object()
