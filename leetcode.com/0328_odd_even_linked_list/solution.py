# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        node = head

        odd_node = ListNode(None)
        eve_node = ListNode(None)

        new_head = odd_node
        eve_head = eve_node

        i = 0

        while node:

            if i % 2 == 0:
                odd_node.next = ListNode(node.val)
                odd_node = odd_node.next
            else:
                eve_node.next = ListNode(node.val)
                eve_node = eve_node.next

            i += 1
            node = node.next

        odd_node.next = eve_head.next
        return new_head.next
