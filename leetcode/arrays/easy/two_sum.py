# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

"""
    INPUTS/OUTPUTS
        nums = [2, 7, 11, 15], target = 9 => [0, 1]

    NOTES
        have a start and end pointer
        use the two to loop through the array twice
        if start and end == target, append it to a new list

"""


def twoSum(nums, target):
    start_pointer = 0
    end_pointer = len(nums) - 1
    result = []

    while start_pointer <= end_pointer:
        current_sum = nums[start_pointer] + nums[end_pointer]
        if current_sum < target:
            start_pointer += 1
        elif current_sum > target:
            end_pointer -= 1
        else:
            result.append([start_pointer, end_pointer])

    return result
