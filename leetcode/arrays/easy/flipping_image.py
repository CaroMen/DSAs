# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.

# For example, flipping [1,1,0] horizontally results in [0,1,1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

# For example, inverting [0,1,1] results in [1,0,0].

"""
    [
        [1,1,0],
        [1,0,1],
        [0,0,0]
    ]

    [
        [1,0,0],
        [0,1,0],
        [1,1,1]
    ]

    NOTES:
        - we can have a row pointer and maybe a column pointer
        - we can start at row 0 and then use the column pointer to flip the elements
        - the way we can flip them is by using reverse()
        - if element is 0, switch it to 1 and vice versa

"""


def flipAndInvertImage(image):
    res = []

    for idx in range(len(image)):
        row = image[idx]
        reverse_row = list(reversed(row))

        for col in range(len(reverse_row)):

            if reverse_row[col] == 0:
                reverse_row[col] = 1
            elif reverse_row[col] == 1:
                reverse_row[col] = 0

        res.append(reverse_row)

    print(res)


flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]])
flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]])
