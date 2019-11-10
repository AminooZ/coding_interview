import pytest

from arrays_and_strings.rotate_matrix import rotate_index, rotate_matrix


@pytest.mark.parametrize("abscissa,ordinate,size,expected", [
    (0, 0, 3, (0, 2)),
    (0, 2, 3, (2, 2)),
    (2, 2, 3, (2, 0)),
    (2, 0, 3, (0, 0)),
    (0, 1, 3, (1, 2)),
    (1, 2, 3, (2, 1)),
    (2, 1, 3, (1, 0)),
    (1, 0, 3, (0, 1)),
    (1, 1, 3, (1, 1)),
    (0, 0, 2, (0, 1)),
])
def test_rotate_index(abscissa, ordinate, size, expected):
    assert rotate_index(abscissa=abscissa, ordinate=ordinate, size=size) == expected


@pytest.mark.parametrize("matrix,expected", [
    (
            [[1, 2],
             [4, 3]],
            [[4, 1],
             [3, 2]],
    ),
    (
            [[1, 2, 3],
             [8, 9, 4],
             [7, 6, 5]],
            [[7, 8, 1],
             [6, 9, 2],
             [5, 4, 3]],
    ),
    (
            [[1, 1, 2, 2],
             [1, 1, 2, 2],
             [3, 3, 4, 4],
             [3, 3, 4, 4]],
            [[3, 3, 1, 1],
             [3, 3, 1, 1],
             [4, 4, 2, 2],
             [4, 4, 2, 2]]
    )
])
def test_rotate_matrix(matrix, expected):
    assert rotate_matrix(matrix=matrix) == expected
