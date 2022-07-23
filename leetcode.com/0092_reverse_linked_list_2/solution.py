class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        values = values[:left-1] + values[left-1:right][::-1] + values[right:]

        head = node = ListNode()
        for v in values:
            node.next = ListNode(v)
            node = node.next

        return head.next
