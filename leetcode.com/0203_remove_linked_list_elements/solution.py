# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        node = head

        # skip begin of target
        while node and node.val == val:
            node = node.next

        nh = node
        prev = node

        while node:

            if node.val == val:
                prev.next = node.next
            else:
                prev = node

            node = node.next

        return nh
