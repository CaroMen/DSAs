# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

"""
    INPUTS/OUTPUTS
        x = 121 => true

        x = -121 => false
            - pay attention to the negative before it

        x = 10 => false

    NOTES
        - ask if we can store the numbers in a list
        - if we can, then we can use pointers and check that the start and end match
        - we need to convert it to string before doing any pointers

"""

# CONVERT TO STRING


def isPalindrome(x):
    num_list = list(str(x))

    start_pointer = 0
    end_pointer = len(num_list) - 1

    while start_pointer <= end_pointer:
        if num_list[start_pointer] != num_list[end_pointer]:
            return False
        start_pointer += 1
        end_pointer -= 1

    return True
