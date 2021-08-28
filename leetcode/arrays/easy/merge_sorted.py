# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


"""
    INPUTS/OUTPUTS
        nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3 => [1, 2, 2, 3, 5, 6]

    NOTES
        - we want to get the last index of nums1 which will be m + n - 1
        - we need a while loop where m > 0 and n > 0
        - check if nums1 is greater than nums2
            - if it is, insert nums1[m] to nums1 at the last idx
            - if not, insert nums2[n] to nums1 at the last idx
        - also check if there are any remaining numbers in nums2
            - this would happen if the first num in nums1 is greater than the first num in nums1

"""


def merge(nums1, nums2):
    last_idx = m + n - 1  # - 1 to account for index starting at 0

    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1

        last_idx -= 1

    while n > 0:
        nums1[last] = nums2[n - 1]
        n -= 1
        last_idx -= 1
