# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

"""
    INPUTS/OUTPUTS
        "()[]{}" => true
            s[s] and s[s - 1] fit

    NOTES:
        i could have a variable named "front" that contains "(" and another named "back" that contains ")"

        loop through s and compare the prev element to see if it matches front
        compare the current element to see if it matches back

        if it does, return true (?)
            * might be some things missing with the logic
"""


def isValid(s):
    front = "("
    back = ")"

    for idx in range(1, len(s)):
        if s[idx - 1] == front and s[idx] == back:
            print(True)
            return True
    print(False)
    return False


isValid("()[]{}")
isValid("(]")
isValid("([)]")
isValid("{[]}")
