class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        old = []
        while head:
            old.append(head.val)
            head = head.next

        new = [old[-1]]
        for i in range(len(old) - 2, -1, -1):
            if old[i] >= new[-1]:
                new.append(old[i])

        head = node = ListNode()
        for n in reversed(new):
            node.next = ListNode(n)
            node = node.next

        return head.next
