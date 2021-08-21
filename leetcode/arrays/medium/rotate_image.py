# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""
    INPUT/OUTPUT
        [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
"""


def rotate(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    last_col = matrix[0][-1]
    first_col = matrix[0][0]

    for row in range(rows):
        for col in range(row):
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp

    """
        [
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9]
        ]

        we need to then swap the first and last num in the rows
    """

    for row in range(rows):
        # print(rows - 1)
        for col in range(rows//2):
            print(col)
            temp = matrix[row][col]
            # rows - 1 to offset the indices starting at 0
            matrix[row][col] = matrix[row][rows - 1 - col]
            matrix[row][rows - 1 - col] = temp

    print(matrix)


rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
