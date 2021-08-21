# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

"""
    INPUTS/OUTPUTS
        s = "anagram", t = "nagaram"
"""


def isAnagram(s, t):
    char_freq = {}

    for char in s:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1

    for char2 in t:
        if char2 not in char_freq:
            return False
        else:
            char_freq[char2] -= 1

    for value in char_freq.values():
        if value != 0:
            return False
    return True


isAnagram("anagram", "nagaram")

# Time complexity - O(n + m + y)
