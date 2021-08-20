# Given a string s and an integer array indices of the same length.

# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

# Return the shuffled string.

# NOTES
#   we can split the string and work with that list
#   possibly swap the strings?
#   since they're the same length, we can have a pointer for both and just loop through one array
#   find the index of


def restoreString(s, indices):
    res = [''] * len(s)

    for idx, char in enumerate(s):
        # insert at the indices[idx] the char
        # so if our first num in indices is 4, it will insert char at the index 4 of res
        res[indices[idx]] = char

    print(''.join(res))
    return ''.join(res)


restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3])
