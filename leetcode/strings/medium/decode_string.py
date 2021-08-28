# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

"""
    INPUTS/OUTPUTS
        s = "3[a]2[bc]" => "aaabcbc"
        s = "3[a2[c]] = > "aaccaccacc"
            - we start from the inner function and spread out

    NOTES
        two main cases:
            - if char is not closing bracket, add to stack
            - if we do find a closing bracket:
                - don't add it to the stack, but do pop from the stack until we get to the opening bracket
                - once we find the opening bracket, we need to get the integer before it
"""


def decodeString(s):
    stack = []

    for idx in range(len(s)):
        if s[idx] != ']':
            stack.append(s[idx])
        else:
            substring = ""
            while stack[-1] != '[':
                substring = stack.pop() + substring
            stack.pop()

            integer = ""
            while stack and stack[-1].isdigit():
                integer = stack.pop() + integer

            stack.append(int(integer) * substring)

    return ''.join(stack)

# Time complexity
