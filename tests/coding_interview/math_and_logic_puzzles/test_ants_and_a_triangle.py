import pytest

from coding_interview.math_and_logic_puzzles.ants_and_a_triangle import \
    ants_and_a_triangle


@pytest.mark.parametrize("n, expected", [
    (3, 0.75)
])
def test_ants_and_a_triangle(n, expected):
    assert ants_and_a_triangle(n=n) == expected
