class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []

        while head:
            values.append(head.val)
            head = head.next

        values.sort()

        head = node = ListNode()

        for n in values:
            node.next = ListNode(n)
            node = node.next

        return head.next
