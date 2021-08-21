# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

"""
    INPUTS/OUPUTS
        [1, 2, 3, 4]
        res:

    NOTES
        we need to take the product of everything to the left and to the right
"""


def productExceptSelf(nums):
    res = [1] * len(nums)

    prefix = 1

    for idx in range(len(nums)):
        # first num has nothing to the left so we set it to the prefix of 1
        res[idx] = prefix
        prefix *= nums[idx]

    postfix = 1

    for idx in reversed(range(len(nums))):
        res[idx] *= postfix
        postfix *= nums[idx]

    return res

# 1 [1, 2, 3, 4] 1
# prefix 1
#   [1]
# prefix 1 * 1
#   [1, 1]
# prefix 1 * 2
#   [1, 1, 2]
# prefix 2 * 3
#   [1, 1, 2, 6]
# postfix = 1
