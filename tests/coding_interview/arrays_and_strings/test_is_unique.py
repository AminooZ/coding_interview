import pytest

from coding_interview.arrays_and_strings.is_unique import is_unique_first_attempt, \
    is_unique_second_attempt, is_unique_third_attempt


@pytest.mark.parametrize("string,unique", [('amine', True),
                                           ('mohamed', False),
                                           ('chocolate', False)])
def test_is_unique_first_attempt(string, unique):
    assert is_unique_first_attempt(string=string) == unique


@pytest.mark.parametrize("string,unique", [('amine', True),
                                           ('mohamed', False),
                                           ('chocolate', False)])
def test_is_unique_second_attempt(string, unique):
    assert is_unique_second_attempt(string=string) == unique


@pytest.mark.parametrize("string,unique", [('amine', True),
                                           ('mohamed', False),
                                           ('chocolate', False)])
def test_is_unique_third_attempt(string, unique):
    assert is_unique_third_attempt(string=string) == unique
