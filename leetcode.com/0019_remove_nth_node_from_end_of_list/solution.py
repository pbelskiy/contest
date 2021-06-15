# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = 0

        node = head
        while node:
            l += 1
            node = node.next

        n = l - n

        prev = None
        node = head

        while node:
            if n == 0:
                if not prev:
                    head = node.next
                else:
                    prev.next = node.next

                break

            n -= 1
            prev = node
            node = node.next

        return head
