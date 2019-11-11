import pytest

from coding_interview.math_and_logic_puzzles.the_100_lockers import get_divisors, \
    get_prime_numbers_under_100, prime_decomposition, the_100_lockers, \
    the_100_lockers_naive, the_100_lockers_less_naive


@pytest.mark.parametrize("number, expected", [
    (15, [1, 3, 5, 15]),
    (8, [1, 2, 4, 8]),
    (12, [1, 2, 3, 4, 6, 12])
])
def test_get_divisors(number, expected):
    assert get_divisors(number=number) == expected


@pytest.mark.parametrize("number, expected", [
    (15, [3, 5]),
    (98, [2, 7, 7]),
    (80, [2, 2, 2, 2, 5]),
    (81, [3, 3, 3, 3]),
    (100, [2, 2, 5, 5])
])
def test_prime_decomposition(number, expected):
    assert prime_decomposition(
        number=number,
        get_prime_numbers_fn=get_prime_numbers_under_100
    ) == expected


def test_the_100_lockers_naive():
    assert the_100_lockers_naive() == 10


def test_the_100_lockers_less_naive():
    assert the_100_lockers_less_naive() == 10


def test_the_100_lockers():
    assert the_100_lockers() == 10
