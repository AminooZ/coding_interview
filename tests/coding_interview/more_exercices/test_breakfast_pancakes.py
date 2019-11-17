import pytest

from coding_interview.more_exercices.breakfast_pancakes import get_minimum_finish_time


@pytest.mark.parametrize("non_empty_plates, expected", [
    ([1], 1),
    ([1, 1], 1),
    ([1, 2], 2),
    ([1, 3], 3),
    ([1, 2, 3], 3),
    ([1, 1, 4], 3),
    ([4, 8, 8], 6)
])
def test_get_minimum_finish_time(non_empty_plates, expected):
    assert get_minimum_finish_time(non_empty_plates=non_empty_plates) == expected
