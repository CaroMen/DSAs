# Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

# Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

"""
    INPUTS/OUTPUTS
        numbers = [2, 7, 11, 15], target = 9 => [1, 2]
            num at index 1 == 2
            num at index 2 == 7

    NOTES
        here we are acting as though indices start at 1, so we need to take that into account

        we might be able to have a start and end pointer and compare the values there to see if they sum up to the target number

        while start is less than end
            create a current sum where numbers[start] + numbers[end]
            if current sum == target
                append to res start + 1, end + 1

            if current sum is less than target
                increment start
            if current sum is greater than target
                decrement end
"""


def twoSum(numbers, target):
    pass
