# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

"""
    INPUTS/OUPUTS
        nums = [1, 2, 3, 1] => true
"""


def containsDuplicate(nums):
    remove_duplicates = set(nums)

    if len(nums) != len(remove_duplicates):
        return True
    return False

# Time complexity is O(n)

# def containsDuplicate(nums):
#     freq = {}

#     for num in nums:
#         if num in freq:
#             return True
#         freq[num] = True
#     return False


# containsDuplicate([1, 2, 3, 1])
