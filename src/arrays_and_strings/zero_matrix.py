# Write an algorithm such that if an element in an MxN matrix is 0, its entire row
# and column are set to 0.


def zero_matrix(matrix):
    # Complexity:
    #       Time:   O(NxM)
    #       Memory: O(1)
    first_row_is_zero = 0 in matrix[0]
    for row in range(1, len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == 0:
                matrix[0][column] = 0
                matrix[row][0] = 0
    for row in range(1, len(matrix)):
        for column in range(1, len(matrix[0])):
            if matrix[row][0] == 0 or matrix[0][column] == 0:
                matrix[row][column] = 0
    if matrix[0][0] == 0:
        for row in matrix:
            row[0] = 0
    if first_row_is_zero:
        matrix[0] = [0 for _ in range(len(matrix[0]))]
    return matrix
