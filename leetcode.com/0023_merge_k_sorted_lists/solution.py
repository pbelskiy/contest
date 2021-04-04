# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        values = []

        for l in lists:
            node = l
            while node:
                values.append(node.val)
                node = node.next


        root = None
        prev = None

        for v in sorted(values):
            node = ListNode(v)
            if not root:
                root = node

            if prev:
                prev.next = node
            prev = node

        return root
