# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

"""
    INPUTS/OUTPUTS:
        s = "hello => "holle"
        s = "leetcode" => leotcede
            a_pointer = "e", b_pointer = "e"
            s = "leetcode"
            a_pointer = "e", b_pointer = "o"
            s = "leotcede"

    NOTES:
        have var with all vowels
        pointer at start and end
        while start <= end:
            if s[start] in vowels and s[end] in vowels:
                temp = s[start]
                s[start] = s[end]
                s[end] = temp
            elif s[start] in vowel and s[end] not in vowels:
                end -= 1
            elif s[start] not in vowel and s[end] in vowel:
                start +=1
        if char in vowel var, we need to switch those

"""


def reverseVowel(s):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    s = list(s)
    start = 0
    end = len(s) - 1

    while start < end:
        if s[start] in vowels and s[end] in vowels:
            # temp = s[start]
            # s[start] = s[end]
            # s[end] = temp
            s[start], s[end] = s[end], s[start]
            end -= 1
            start += 1
        elif s[end] not in vowels:
            end -= 1
        elif s[start] not in vowels:
            start += 1
    print(s)


reverseVowel('hello')
