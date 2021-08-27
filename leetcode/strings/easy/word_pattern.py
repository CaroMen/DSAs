# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

"""
    INPUTS/OUTPUTS
        pattern = "abba", s = "dog cat cat dog" => true
            - in this instance "dog" is the same as "a"
            - "cat" is the same as "b"
            - the pattern here is the first and last words need to be the same
            - and the inner words need to be the same as well

        pattern = "abba", s = "dog cat cat fish" => false

        pattern = "aaaa", s = "dog cat cat dog" => false

        NOTES:
            we map the letters in s to the word in pattern, so we could use the hashmap
            we can split the s and get just the words
            we can check if the length of pattern and s_split dont match, then return false right away
            we can loop through the pattern and fill in our hashmap with the keys
                if there's a value for the key, check to see if the value matches the word[i]
                    if it doesnt return False
                else, set the key equal to the word in word[i]
                    also check if the word[i] is in the hashmap and if it is return false

"""


def word_pattern(pattern, s):
    s_list = s.split(' ')

    if len(pattern) != len(s_list):
        return False

    map_pattern = {}

    for idx in range(len(list(pattern))):
        char = pattern[idx]
        if char in map_pattern:
            if map_pattern[char] != s_list[idx]:
                return False
        else:
            if s_list[idx] in map_pattern:
                return False
            map_pattern[char] = s_list[idx]

    return True


word_pattern("abba", "dog cat cat dog")
