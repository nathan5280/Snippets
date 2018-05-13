import pytest
import random


@pytest.fixture()
def expensive_setup():
    """
    This fixture is run for every test case.

    :return: Random integer.
    """
    print("\nExpensive Setup...")

    # Do something expensive that only needs to be done once pre class.
    for _ in range(0, 100000):
        pass

    return random.randint(1, 100)


@pytest.fixture(scope="class")
def expensive_setup_class():
    """
    Some test resources are expensive to create and can be reused across tests.

    This fixture is only run once per class.

    :return: Random integer.
    """
    print("\nExpensive Setup (class)...")

    # Do something expensive that only needs to be done once pre class.
    for _ in range(0, 100000):
        pass

    return random.randint(1, 100)


class TestClass1:
    # Note that test classes can't have an __init__ method.
    # def __init__(self):
    #     print("TestClass1")

    def test_one(self, expensive_setup: int, expensive_setup_class: int) -> None:
        print("TestClass1:test_one (no scope): ", expensive_setup)
        print("TestClass1:test_one (class scope): ", expensive_setup_class)

    def test_two(self, expensive_setup: int, expensive_setup_class: int) -> None:
        print("TestClass1:test_two (no scope): ", expensive_setup)
        print("TestClass1:test_two (class scope): ", expensive_setup_class)

class TestClass2:
    def test_one(self, expensive_setup: int, expensive_setup_class: int) -> None:
        print("TestClass2:test_one (no scope): ", expensive_setup)
        print("TestClass2:test_one (class scope): ", expensive_setup_class)

    def test_two(self, expensive_setup: int, expensive_setup_class: int) -> None:
        print("TestClass2:test_two (no scope): ", expensive_setup)
        print("TestClass2:test_two (class scope): ", expensive_setup_class)
