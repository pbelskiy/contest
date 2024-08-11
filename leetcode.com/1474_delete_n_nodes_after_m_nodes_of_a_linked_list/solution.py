class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        node = head

        while node:
            i = 0

            # skip
            while node and i < m - 1:
                i += 1
                node = node.next

            # delete
            i = 0
            curr = node
            while node and i <= n:
                i += 1
                node = node.next

            if curr:
                curr.next = node

        return head
