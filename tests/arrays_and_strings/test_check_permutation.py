import pytest

from arrays_and_strings.check_permutation import check_permutation_first_attempt, \
    check_permutation_second_attempt


@pytest.mark.parametrize("left,right,expected",
                         [('AZERTY', 'YTREZA', True),
                          ('permutation', 'check', False)])
def test_check_permutation_first_attempt(left, right, expected):
    assert check_permutation_first_attempt(left=left, right=right) == expected


@pytest.mark.parametrize("left,right,expected",
                         [('AZERTY', 'YTREZA', True),
                          ('permutation', 'check', False)])
def test_check_permutation_second_attempt(left, right, expected):
    assert check_permutation_second_attempt(left=left, right=right) == expected
