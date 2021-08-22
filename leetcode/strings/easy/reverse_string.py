# Write a function that reverses a string. The input string is given as an array of characters s.

"""
    INPUTS/OUTPUTS
        ["h", "e", "l", "l", "o"] => ["o", "l", "l", "e", 'h"]

    NOTES
        brute force solution could be to create a new list, iterate backwards through the list, appeand each element to the new list
        Time complexity: O(n)
        Space complexity: O(n)

        better way of solving it is to have two pointers, one pointing at the front and one pointing at the back. Instead of creating a new array, I could just swap using those two pointers
        Time complexity: O(n)
        Space complexity: O(1)
"""


def reverseString(s):
    start_pointer = 0
    end_pointer = len(s) - 1

    while start_pointer <= end_pointer:
        temp = s[start_pointer]
        s[start_pointer] = s[end_pointer]
        s[end_pointer] = temp

        start_pointer += 1
        end_pointer -= 1

    print(s)


reverseString(["h", "e", "l", "l", "o"])
