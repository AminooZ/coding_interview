import pytest

from coding_interview.arrays_and_strings.one_away import one_away


@pytest.mark.parametrize("word_a, word_b,expected", [('pale', 'ple', True),
                                                     ('pales', 'pale', True),
                                                     ('pale', 'bale', True),
                                                     ('pale', 'bake', False),
                                                     ('zoo', 'moo', True),
                                                     ('da', 'data', False)])
def test_one_away(word_a, word_b, expected):
    assert one_away(word_a=word_a, word_b=word_b) == expected
