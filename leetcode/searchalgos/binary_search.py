"""
    Given an array of integers nums which is sorted in ascending order and an integer target, write a function nums. If target exists, then return its index. Otherwise, return -1

    You must write an algorithm with O(log n) runtime complexity


    INPUTS/OUTPUTS
        nums = [-1, 0, 3, 5, 9, 12], target = 9 => 4
        nums = [-1, 0, 3, 5, 9, 12], target = 2 => -1

    NOTES
        - create a variable to find the middle of the array/list
        - we check if the middle number equals the target number
        - based on where the middle number falls, either less than or greater than the target number, we check the left or right side of the list
        - repeat this process until the middle number is equal to the target number or until the list is empty

"""

def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2
        current_num = nums[middle]

        if current_num == target:
            return middle
        elif current_num > target: # we are dealing with the right side now
            right = middle - 1
        elif current_num < target: # we are dealing with the left side now
            left = middle + 1

    return -1
