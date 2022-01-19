class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()

        while head:
            if head in visited:
                return head

            visited.add(head)
            head = head.next

        return None
