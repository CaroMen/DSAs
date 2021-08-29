# Given a string s, find the length of the longest substring without repeating characters.

"""
    INPUTS/OUTPUTS
        s = "abcabcbb"

    NOTES
        approach one:
            use a hashmap to map every letter with the count of their appearance
            if the value of one goes up to 2, we should start from scratch so the letters aren't repeating
            start from scratch would mean, erasing the contents of the hashmap but continuing to loop where we left off, so the hashmap should only contain the letter that made our value go up to 2
"""

# abcab
# start = a
# end = a


def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    result = 0

    for right in range(len(s)):
        # if letter exists in set, then remove the first letter at the start pointer and increment start pointer
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        result = max(result, right - left + 1)

    return result


lengthOfLongestSubstring("abcabcbb")
