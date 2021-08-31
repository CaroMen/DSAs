# Given the head of a singly linked list, reverse the list, and return the reversed list.

"""
    INPUTS/OUTPUTS
        head = [1, 2, 3, 4, 5] => [5, 4, 3, 2, 1]

    NOTES
        we need to make our head point to None
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(head):
        # 1 -> 2 -> 3
        # previous is None
        # current is 1
        previous, current = None, head

        while current:
            # store the value where the connection is going to be broken
            # next_node is 2
            next_node = current.next
            # 2 .next points to None now
            current.next = previous
            # previous should now be the current we had
            # previous is now 1
            previous = current
            current = next_node

        return previous
