class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # reverse right half
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # merge
        l1, l2 = head, prev
        while l1 and l2:
            n1, n2 = l1.next, l2.next
            l1.next,  l2.next = l2, n1
            l1, l2 = n1, n2
