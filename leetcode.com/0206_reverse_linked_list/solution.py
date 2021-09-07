class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        head = ListNode()
        node = head

        for val in reversed(values):
            node.next = ListNode(val)
            node = node.next

        return head.next
