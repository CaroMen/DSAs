# Given a 2D integer array matrix, return the transpose of matrix.

# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
"""
    INPUTS/OUTPUTS
        [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ] =>
        [
            [1,4,7],
            [2,5,8],
            [3,6,9]
        ]

    Challenge: Try doing it in place by swapping the elements?
"""


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    # we need to multiply it by rows because the inner lists are the
    # rows
    new_matrix = [[0] * rows for _ in range(cols)]

    for row in range(rows):
        for col in range(cols):
            new_matrix[col][row] = matrix[row][col]

    return new_matrix


"""
only works if the shape of the matrix stays the same

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        for col in range(cols):
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp

transpose([[1,2,3],[4,5,6],[7,8,9]])
"""
