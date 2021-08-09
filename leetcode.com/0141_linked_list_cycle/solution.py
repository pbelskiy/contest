class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()

        while head:
            if head in visited:
                return True

            visited.add(head)
            head = head.next

        return False
