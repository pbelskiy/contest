# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        target = curr = prev = None

        curr = head

        while curr:
            if curr.next and curr.next.val == curr.val:
                target = curr.val

            if curr.val != target:
                prev = curr
                curr = curr.next
                continue

            while curr and curr.val == target:
                if curr == head:
                    head = curr.next
                    curr = head
                else:
                    curr = curr.next
                    prev.next = curr

        return head
