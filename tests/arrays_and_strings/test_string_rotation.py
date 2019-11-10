import pytest

from arrays_and_strings.string_rotation import string_rotation


@pytest.mark.parametrize("string1, string2,expected", [
    ('waterbottle','erbottlewat', True),
    ('blop', 'blopa', False),
    ('pale', 'lepa', True),
    ('pale', 'bake', False),
    ('data', 'daat', False),
    ('da', 'ada', False)])
def test_string_rotation(string1, string2, expected):
    assert string_rotation(string1=string1, string2=string2) == expected
