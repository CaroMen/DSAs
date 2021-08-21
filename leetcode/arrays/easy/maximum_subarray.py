# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

"""
    INPUTS/OUTPUTS
        [-2,1,-3,4,-1,2,1,-5,4] => 6

    NOTES
        we could use the sliding window technique
        we need to return the sum
        ! Used Kadane's algorithm
"""


def maxSubArray(nums):
    max_sum = 0  # final return
    current_max = 0  # used this to compare the current max and final max

    for idx in range(1, len(nums)):
        current_num = nums[idx]
        current_max = max(current_num, current_num + current_max)
        max_sum = max(max_sum, current_max)

    return max_sum


maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
