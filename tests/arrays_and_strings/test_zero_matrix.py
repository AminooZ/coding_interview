import pytest

from arrays_and_strings.zero_matrix import zero_matrix


@pytest.mark.parametrize("matrix,expected", [
    ([[1, 1],
      [1, 1]],
     [[1, 1],
      [1, 1]]
     ),
    ([[1, 1, 1],
      [1, 0, 1],
      [1, 1, 1]],
     [[1, 0, 1],
      [0, 0, 0],
      [1, 0, 1]]),
    ([[0, 1, 1, 1],
      [1, 0, 1, 1],
      [1, 1, 0, 1],
      [1, 1, 1, 0]],
     [[0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0]])
])
def test_zero_matrix(matrix, expected):
    assert zero_matrix(matrix=matrix) == expected
