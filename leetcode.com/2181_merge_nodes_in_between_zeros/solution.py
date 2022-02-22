class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = c = ListNode(0)

        while head:
            if head.val:
                c.val += head.val

            elif c.val and head.next:
                c.next = ListNode(0)
                c = c.next

            head = head.next

        return h
