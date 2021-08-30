# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

"""
    INPUTS/OUTPUTS
        nums = [-1, 0, 1, 2, -1, -4] => [[-1, -1, 2], [-1, 0, 1]]
            [nums[i], nums[j], nums[k]]
            [ -1    , -1     , 2      ]
            -1 != -1 (??)
            -1 != 2 (good)
            -1 != 2 (good)
    NOTES
        brute force solution would be nested loops to get 3 numbers, make sure each doesnt equal to each other, and append them to a list
"""
