# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.

# For example, flipping [1,1,0] horizontally results in [0,1,1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

# For example, inverting [0,1,1] results in [1,0,0].


"""
    INPUTS/OUTPUTS
        image = [
            [1, 1, 0],
            [1, 0, 1],
            [0, 0, 0]
        ]
        =>
        [
            [1, 0, 0],
            [0, 1, 0],
            [1, 1, 1]
        ]

    NOTES
        each 1 needs to be turned into a 0
        each 0 needs to be turned into a 1
        the values inside the inner lists have to be reversed

        we might not be able to use just one for loop
        so, I'd loop through the outer list and use a variable to store the inner lists
            for idx in range(len(image)):
                current_row = image[idx]

        each row has to be reversed, so I might use the reversed() method. we can also store this in a variable
            - no clue what the reversed method returns so review that

        using that variable, I'd loop through the inner lists, which should now be reversed

        check each value to see if it's 0 or 1 and then flip those around
            - so 1 turns to 0, 0 turns to 1

"""


def flipAndInvert(image):
    result = []

    for idx in range(len(image)):
        current_row = image[idx]
        reversed_list = list(reversed(current_row))

        for idx in range(len(reversed_list)):

            if reversed_list[idx] == 1:
                reversed_list[idx] = 0
            elif reversed_list[idx] == 0:
                reversed_list[idx] = 1

        result.append(reversed_list)

    print(result)
    return result


flipAndInvert([[1, 1, 0], [1, 0, 1], [0, 0, 0]])
