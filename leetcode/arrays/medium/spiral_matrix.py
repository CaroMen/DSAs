# Given an m x n matrix, return all elements of the matrix in spiral order.

"""
    INPUTS/OUTPUTS
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        =>

        [1, 2, 3, 6, 9, 8, 7, 4, 5]

    NOTES
        return a list of the traversal
        is it always going to be a square? so same amount of rows and columns?

        INITIAL THOUGHTS
            nested loops
            have a hard time figuring out how i'd determine the edges

        SECOND THOUGHT
            have a result variable equal to []

            two pointers pattern
                - one for outer list to track each row
                - one for inner list to track each column

                row_start = 0
                row_end = len(matrix) - 1

                col_start = 0
                col_end = len(matrix[0]) - 1

            ! do a while loop where col_start <= col_end AND row_start <= row_end

            we need the first numbers on row one -> kinda tricky, but we need to loop through the columns to get each number
                for col in range(len(col_start, col_end + 1)):
                    result.append(matrix[row_start][col])

            we need to now get the numbers on the right most column.
                - we need to make sure we dont check the "row" we just went through, so do row_start + 1
                for row in range(len(row_start + 1, row_end + 1)):
                    result.append(matrix[row][col_end])

            we need to now go to the last row and grab each number at the columns
                - again, we need to make sure we don't check numbers we already have
                for col in range(len(col_start, col_end)):
                    result.append(matrix[row_end][col])

            we need to get the numbers in the first column now
                - we need to make sure we don't get the first number in the column, so we do row_start + 1
                for row in range(len(row_start + 1, row_end))
                    result.append(matrix[row][col_start])

"""


def spiralOrder(matrix):
    result = []

    row_start, row_end = 0, len(matrix) - 1
    col_start, col_end = 0, len(matrix[0]) - 1

    while row_start <= row_end and col_start <= col_end:
        for col in range(col_start, col_end + 1):
            result.append(matrix[row_start][col])

        for row in range(row_start + 1, row_end + 1):
            result.append(matrix[row][col_end])

        for col in reversed(range(col_start, col_end)):
            if row_start == row_end:
                break
            result.append(matrix[row_end][col])

        for row in reversed(range(row_start + 1, row_end)):
            if col_start == col_end:
                break
            result.append(matrix[row][col_start])

        row_start += 1
        row_end -= 1
        col_start += 1
        col_end -= 1

    return result
