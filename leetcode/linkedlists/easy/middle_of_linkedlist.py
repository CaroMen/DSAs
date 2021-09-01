# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

"""
    INPUTS/OUTPUTS
        head = [1, 2, 3, 4, 5] => [3, 4, 5]

        head = [1, 2, 3, 4, 5, 6] => [4, 5, 6]

    NOTES
        - if we have two middle points, we need to return the second middle
        - we can use the fast and slow pointer pattern
        - we might be able to loop as normal with one pointer moving two ahead and the other moving one at a time
        - then once the fast pointer reaches the end, our slow pointer should be the halfway point (?)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        fast = head
        slow = head
        while fast is not None and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
