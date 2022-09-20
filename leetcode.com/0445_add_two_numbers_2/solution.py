class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = '', ''

        while l1:
            n1 += str(l1.val)
            l1 = l1.next

        while l2:
            n2 += str(l2.val)
            l2 = l2.next

        head = node = ListNode()

        for d in list(str(int(n1) + int(n2))):
            node.next = ListNode(int(d))
            node = node.next

        return head.next
