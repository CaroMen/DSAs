# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

# INPUTS/OUTPUTS
#   nums = [1, 2, 3, 4] => [1, 3, 6, 10]
#   obtained by doing [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 +4]

# NOTES
#   we can keep a sum variable
#   loop starting from index 1
#   append to the new array the sums

def runningSum(nums):
    new_array = [nums[0]]
    sum = nums[0]

    for i in range(1, len(nums)):
        sum += nums[i]
        new_array.append(sum)

    return new_array

# Time Complexity = O(n)
# Space Complexity = O(n)
