class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast, prev = head, head, head

        while slow and fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if not prev.next:
            return None

        prev.next = prev.next.next
        return head
