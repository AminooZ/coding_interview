import pytest

from coding_interview.math_and_logic_puzzles.the_apocalypse import \
    set_gender_probability, the_apocalypse


@pytest.mark.parametrize("nb_experiments, boy_probability", [
    (1000, 0.5),
    (1000, 0.2)
])
def test_set_gender_probability(nb_experiments, boy_probability):
    get_gender_fn = set_gender_probability(boy_probability=boy_probability)
    boys_count = 0
    for _ in range(nb_experiments):
        boys_count += get_gender_fn() == 'B'

    assert boys_count / nb_experiments == pytest.approx(boy_probability, 0.1)


@pytest.mark.parametrize("families_count, boy_probability", [
    (1000, 0.5),
    (5000, 0.2)
])
def test_the_apocalypse(families_count, boy_probability):
    assert the_apocalypse(families_count=families_count,
                          get_gender_fn=set_gender_probability(
                              boy_probability=boy_probability)
                          ) == pytest.approx(boy_probability, 0.1)
