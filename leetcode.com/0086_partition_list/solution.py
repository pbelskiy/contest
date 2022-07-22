class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = []
        right = []

        while head:
            if head.val < x:
                left.append(head.val)
            else:
                right.append(head.val)
            head = head.next

        head = node = ListNode()
        for v in left + right:
            node.next = ListNode(v)
            node = node.next

        return head.next
