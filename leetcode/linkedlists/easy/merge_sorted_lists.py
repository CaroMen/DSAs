# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

"""
    INPUTS/OUTPUTS
        l1 = [1, 2, 4], l2 = [1, 3, 4] => [1, 2, 3, 4, 4]

    NOTES
        - since each linked list is sorted, we can loop through one and compare each value.
        - we then place the lowest value in our new linked list and continue to do that
        - eventually, we might have one linked list that is shorter than the other, so we can just add in the remaining nodes of that linked list
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next

# Time Complexity: O(n)
