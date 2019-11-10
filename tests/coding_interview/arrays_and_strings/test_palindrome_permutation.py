import pytest

from coding_interview.arrays_and_strings.palindrome_permutation import \
    palindrome_permutation_first_attempt, palindrome_permutation_second_attempt


@pytest.mark.parametrize("sentence,expected", [
    ('Tact cao', True),
    ('toto', True),
    ('Aminem', False)
])
def test_palindrome_permutation_first_attempt(sentence, expected):
    assert palindrome_permutation_first_attempt(sentence=sentence) == expected


@pytest.mark.parametrize("sentence,expected", [
    ('Tact cao', True),
    ('toto', True),
    ('Aminem', False)
])
def test_palindrome_permutation_second_attempt(sentence, expected):
    assert palindrome_permutation_second_attempt(sentence=sentence) == expected
