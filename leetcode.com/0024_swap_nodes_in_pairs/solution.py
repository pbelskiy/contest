class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []

        while head:
            values.append(head.val)
            head = head.next

        for i in range(0, len(values) - 1, 2):
            values[i], values[i+1] = values[i+1], values[i]

        head = ListNode()
        node = head

        for v in values:
            node.next = ListNode(v)
            node = node.next

        return head.next
