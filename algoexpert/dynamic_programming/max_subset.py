# write a function that takes in an array of positive integers and returns the maximum sum of non-adjacent elements in the array

# if the input array is empty, the function should return 0

"""
    INPUTS/OUTPUTS
        array = [75, 105, 120, 75, 90, 135] => 330
"""


def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]

    max_sum = array[:]
    max_sum[1] = max(array[0], array[1])

    for i in range(2, len(array)):
        max_sum[i] = max(max_sum[i - 1], max_sum[i - 2] + array[i])

    return max_sum[-1]
