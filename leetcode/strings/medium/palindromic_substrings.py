# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

"""
    INPUTS/OUTPUTS
        s = "abc" => 3
            "a", "b", "c" are palindromes

        s = "aaa" => 6
            "a", "a, "a", "aa", "aa", "aaa"

    NOTES
        very similar to longest palindromic substring problem
        consider each letter as the mid and expand outwards
        create a variable to keep count of the palindromes

    PSEUDOCODE
        count = 0

        for idx in range(len(string))
            left, right = idx, idx

            while left is in bound and right is in bound and left == right
                count += 1
            left -= 1
            right -= 1

            left, right = idx, idx + 1

            while left is in bound and right is in bound and left == right
                count += 1
            left -= 1
            right += 1
        return count
"""


def countSubstrings(s):
    count = 0

    for idx in range(len(s)):
        left, right = idx, idx

        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

        left, right = idx, idx + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    return count
