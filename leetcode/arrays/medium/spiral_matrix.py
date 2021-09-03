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
                    col_start += 1


"""


def spiralOrder(matrix):
    pass
