# Given a string s, return the longest palindromic substring in s.

"""
    INPUTS/OUTPUTS
        s = "babad" => "bab"

    NOTES
        - might need to do a window sliding technique as well
        - we could also use each letter as the "mid" point and expand outward to the left and right
        - if the letter to the left and right match, set that range of letters to the res variable
        - also keep count of the length and update it by doing right - left + 1 (plus 1 to balance out index starting at 0 )
        - there's also the case where the string is even, which means we won't have an actual middle point
        - in this scenario we do the same thing as before, but we need to start our right pointer at i + 1
            - we do i + 1 because we're working with indices
"""


def longestPalindrome(s):
    res = ""
    res_length = 0

    for idx in range(len(s)):
        left, right = idx, idx

        # if string length is odd
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > res_length:
                res = s[left:right+1]
                res_length = right - left + 1
            left -= 1
            right += 1

        left, right = idx, idx + 1

        # if string length is even
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > res_length:
                res = s[left: right+1]
                res_length = right - left + 1
            left -= 1
            right += 1

    return res
