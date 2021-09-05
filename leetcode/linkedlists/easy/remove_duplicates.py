# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

"""
    INPUTS/OUTPUTS
        head = [1, 1, 2] => [1, 2]
        head = [1, 1, 2, 3, 3] => [1, 2, 3]

    NOTES
        questions:
            is it fair to assume that all inputs will be sorted?
            since they're sorted, i can just check if the adjacent node is equal to the previous node?

        - we can set a variable to head and call it current
        - essentially, we can do a while loop while current is not None AND current has a .next
        - we can then reassigned our current.next to current.next.next
            - this basically moves the pointer of our current
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        pass

        # current = head

        # while current and current.next:
        #     if current.val == current.next.val:
        #         current.next = current.next.next
        #     else:
        #         current = current.next

        # return head
