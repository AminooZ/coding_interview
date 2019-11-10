# Given an image represented by an NxN matrix where each pixel in the image is 4 Bytes,
# write a method to rotate the image by 90 degrees. Can you do this inplace ?


def rotate_matrix(matrix):
    # Complexity:
    #       Time:   O(N^2)
    #       Memory: O(N^2)
    size = len(matrix)
    for abscissa in range((size - 1) // 2 + 1):
        for ordinate in range(size // 2):
            abscissa_1, ordinate_1 = rotate_index(
                abscissa=abscissa,
                ordinate=ordinate,
                size=size
            )
            abscissa_2, ordinate_2 = rotate_index(
                abscissa=abscissa_1,
                ordinate=ordinate_1,
                size=size
            )
            abscissa_3, ordinate_3 = rotate_index(
                abscissa=abscissa_2,
                ordinate=ordinate_2,
                size=size
            )
            matrix[abscissa][ordinate], matrix[abscissa_3][ordinate_3], \
            matrix[abscissa_2][ordinate_2], matrix[abscissa_1][ordinate_1] = \
                matrix[abscissa_3][ordinate_3], matrix[abscissa_2][ordinate_2], \
                matrix[abscissa_1][ordinate_1], matrix[abscissa][ordinate]
    return matrix


def rotate_index(abscissa, ordinate, size):
    center = (size - 1) / 2
    abscissa_diff = center - abscissa
    ordinate_diff = center - ordinate
    return int(center - ordinate_diff), int(center + abscissa_diff)
