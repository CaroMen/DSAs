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

        second approach:
            loop through from range 0 to length of nums
            have a length variable and a variable to count total sum of the values inside the nums list
            inside the loop, do sum += nums[idx]
            and also increment the length of the list by idx
            return length - sum

            [0, 2, 3, 4]
                - length is 4
                - missing num is 1
                loop 1:
                    idx - 0
                    sum - 0
                    length - 4
                loop 2:
                    idx - 1
                    sum - 2
                    length - 5 (idx + length)
                loop 3:
                    idx - 2
                    sum - 5
                    length - 7 (idx + length)
                loop 4:
                    idx - 3
                    sum - 9
                    length - 10 (idx + length)

                return lenth (now 10) - sum (9) = 1, our missing number

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
