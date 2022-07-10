import pytest

from coding_interview.arrays_and_strings.string_compression import string_compression


@pytest.mark.parametrize("word,expected", [
    ('aabcccccaaa', 'a2b1c5a3'),
    ('toto', 'toto')
])
def test_string_compression(word, expected):
    assert string_compression(word=word) == expected
