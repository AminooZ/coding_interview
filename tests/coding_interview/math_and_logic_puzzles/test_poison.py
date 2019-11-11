import pytest

from coding_interview.math_and_logic_puzzles.poison import int_to_binary, \
    set_poisoned_bottle, poison


@pytest.mark.parametrize("bottle, bottles, expected", [
    (36, [1, 2, 3, 19], 0),
    (36, [4, 9, 36, 1], 1),
    (42, [4, 9, 36, 1], 0)
])
def test_set_poisoned_bottle(bottle, bottles, expected):
    test_trip_fn = set_poisoned_bottle(bottle=bottle)
    assert test_trip_fn(bottles=bottles) == expected


@pytest.mark.parametrize("number, size, expected", [
    (42, 10, '0000101010'),
    (42, 6, '101010'),
    (800, 10, '1100100000')
])
def test_int_to_binary(number, size, expected):
    assert int_to_binary(number=number, size=size) == expected


@pytest.mark.parametrize("bottle", [
    12,
    42,
    600,
    939,
    999
])
def test_poison(bottle):
    test_strip_fn = set_poisoned_bottle(bottle=bottle)
    assert poison(test_strip_fn=test_strip_fn) == bottle
