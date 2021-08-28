# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

"""
    INPUTS/OUTPUTS
        nums = [3, 0, 1] => 2
            explanation:
                n is 3 because there the length of nums is 3
                2 is the missing num from the range of 0 to 3

        nums = [0, 1]
            explanation:
                n is 2 because length of nums is 2
                2 is the missing num from the range of 0 to 2

    NOTES
        range will always be from 0 to length of nums
        create variable nums_length to hold length of nums
        loop from 0 to nums_length
        if the idx not in nums:
            return idx
"""


def missingNumber(nums):
    length = len(nums)

    for idx in range(0, length + 1):
        if idx not in nums:
            return idx

# Time complexity: O(n), Space Complexity: O(1)


def missingNumber2(nums):
    tracker = 0
    length = len(nums)

    for idx in range(0, len(nums)):
        tracker += nums[idx]
        length += idx

    return len(nums) - tracker
