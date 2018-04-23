from abc import ABC, abstractmethod
from typing import Union


class BaseClass(ABC):
    def __init__(self, idx: int) -> None:
        self.idx = idx  # type : int

    @abstractmethod
    def indexed_announce(self, msg: Union[str, None] = None) -> str:
        pass


class SubClassA(BaseClass):
    def indexed_announce(self, msg: Union[str, None] = None) -> str:
        return "Class A - {}: {}".format(msg, self.idx)


class SubClassB(BaseClass):
    def indexed_announce(self, msg: Union[str, None] = None) -> str:
        return "Class B - {}: {}".format(msg, self.idx)


def announce(cls: BaseClass, msg: str) -> str:
    return cls.indexed_announce(msg)


if __name__ == '__main__':
    a = SubClassA(1)

    print(a.indexed_announce("Hello"))
    print(announce(a, "Hello"))
