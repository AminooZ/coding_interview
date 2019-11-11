from math import factorial

import pytest

from coding_interview.math_and_logic_puzzles.basketball import basketball, combination


@pytest.mark.parametrize("n, k", [
    (4, 1),
    (4, 3),
    (5, 2),
    (10, 2)
])
def test_combination(n, k):
    assert combination(n=n, k=k) == factorial(n) // factorial(k) // factorial(n - k)


@pytest.mark.parametrize("n, k, p, expected", [
    (3, 2, 0.5, 0),
    (3, 2, 0.6, 2),
    (3, 2, 0.4, 1),
    (2, 5, 0.6, 1),
    (2, 9, 0.6, 1)
])
def test_basketball(n, k, p, expected):
    assert basketball(n, k, p) == expected
