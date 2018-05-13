import pytest_

@pytest_.fixture
def prime_list():
    primes = (1,2,3,5,7,11,13)
    return primes


def test_primes(prime_list):
    assert 3 in prime_list

