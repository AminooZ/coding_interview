import pytest

from math_and_logic_puzzles.the_heavy_pill import set_heavy_pill, the_heavy_pill


@pytest.mark.parametrize("heavy_pill", [x for x in range(1, 21)])
def test_set_heavy_pill(heavy_pill):
    get_weight_fn = set_heavy_pill(heavy_pill=heavy_pill)
    assert get_weight_fn(pills={heavy_pill: 1}) == 1.1
    for other_pill in range(1, 21):
        if other_pill != heavy_pill:
            assert get_weight_fn(pills={other_pill: 1}) == 1


@pytest.mark.parametrize("heavy_pill", [x for x in range(1, 21)])
def test_the_heavy_pill(heavy_pill):
    get_weight_fn = set_heavy_pill(heavy_pill=heavy_pill)
    assert the_heavy_pill(get_weight_fn=get_weight_fn) == heavy_pill