# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

"""
    INPUTS/OUTPUTS
        lists = [[1, 4, 5], [1, 3, 4], [2, 6]] =>

    NOTES
        FIRST THOUGHT
            two loops
            one for the outer array
            from there we do essentially the same as the Merge Sorted Lists
            - each list inside of lists is a linked list, so we have to compare each of those to each other


"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(lists):
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []

            for idx in range(0, len(lists), 2):
                lst1 = lists[idx]
                lst2 = lists[idx + 1] if (idx + 1) < len(lists) else None
                mergedLists.append(self.mergeLists(lst1, lst2))

            lists = mergedLists

        return lists[0]

    def mergeLists(self, lst1, lst2):
        dummy = ListNode()
        tail = dummy

        while lst1 and lst2:
            if lst1.val < lst2.val:
                tail.next = lst1
                lst1 = lst1.next
            elif lst1.val > lst2.val:
                tail.next = lst2
                lst2 = lst2.next
            tail = tail.next

        if lst1:
            tail.next = lst1
        elif lst2:
            tail.next = lst2

        return dummy.next
