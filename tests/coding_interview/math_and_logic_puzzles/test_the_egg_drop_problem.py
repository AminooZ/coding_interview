import pytest

from coding_interview.math_and_logic_puzzles.the_egg_drop_problem import set_floor, \
    the_egg_drop_problem


@pytest.mark.parametrize("n, floor", [
    (50, 89),
    (49, 49),
    (42, 39)
])
def test_set_floor(n, floor):
    get_egg_state_fn = set_floor(n=n)
    assert get_egg_state_fn(floor=floor) == (floor >= n)


@pytest.mark.parametrize("floors_count, n", [
    (100, 37),
    (100, 51),
    (100, 89)

])
def test_the_egg_drop_problem(floors_count, n):
    get_egg_state_fn = set_floor(n=n)
    assert the_egg_drop_problem(floors_count=floors_count,
                                get_egg_state_fn=get_egg_state_fn) == n
