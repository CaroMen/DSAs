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
    stack = []
    close_to_open = {")": "(", "}": "{", "]": "["}

    for char in s:
        # this by default loops through the keys, so
        # we're looking at the closing parenthesis
        if char in close_to_open:
            # make sure stack is not empty and that
            # top value is matching opening parenthesis
            if stack and stack[-1] == close_to_open[char]:
                stack.pop()
            else:
                # dont match or stack is empty
                # parenthesis don't match
                print(False)
                return False
        # if we don't get a closing parenthesis
        else:
            # just add open parenthesis to stack
            stack.append(c)

    # return true only if stack is empty
    return True if not stack else False
    # print(stack)


# isValid("()[]{}")
# isValid("(]")
# isValid("([)]")
isValid("{[]}")
