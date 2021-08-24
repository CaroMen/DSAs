# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

"""
    INPUTS/OUTPUTS:
        s = "A man, a plan, a canal: Panama" => true
            "amanaplanacanalpanama" is a palindrome.

    NOTES:
        we could have a start and end pointer that we use to check if the letters match

        ! these test cases have puctuation and we're told to just consider alphanumeric characters

        ! we also have upper and lower case lettes which aren't considered the same, so we need to lower all of them. we could also make them all capital letters

        with this in mind, we need to check if our current letters are alphanumeric by using isalnum()
"""


def isPalindrome(s):
    start = 0
    end = len(s) - 1

    while start <= end:
        left_str = s[start].lower()
        right_str = s[end].lower()

        if left_str.isalnum() and right_str.isalnum():
            if left_str != right_str:
                return False
            start += 1
            end -= 1
        else:
            if not left_str.isalnum():
                start += 1
            if not right_str.isalnum():
                end -= 1

    return True
