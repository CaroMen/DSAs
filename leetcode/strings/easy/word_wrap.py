# NOT LEETCODE
# Given a string, write an algorithm to wrap the whole string so that not more than 8 characters are on one line. Also you have to make sure you don't break/split any word into two. Spaces are considered characters as well.

"""
    INPUTS/OUTPUTS:
        "Hello, my name is Caroline and I am a junior engineer"
        =>
        "Hello,
        my name
        is
        Caroline
        and I am
        a junior
        engineer"

    NOTES:
        we could loop through the string or create a loop through 8
            so: for i in range(8):
            * this wouldn not loop through the entire string
        we have to check that the words aren't being split
            not sure how *

"""


def word_wrap(string, max_width):
    res = []

    for i in range(len(string) - 1):
        # if len(string[i]) <= max_width:
        new_line = string[:max_width]

        if new_line[-1] == ' ':
            res.append(new_line)
            # print(new_line)
        else:
            max_width -= 1

        # print(new_line)
        res.append(new_line.find)
        string = string[max_width:]

        if len(new_line) < max_width:
            break

    print('\n'.join(res))


word_wrap("Hello, my name is Caroline and I am a junior engineer", 8)
