class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = node = ListNode()
        carry = 0

        while l1 and l2:
            total = l1.val + l2.val + carry
            carry = total // 10

            node.next = ListNode(total % 10)
            node = node.next

            l1 = l1.next
            l2 = l2.next

        tail = l1 or l2

        while tail:
            total = tail.val + carry
            carry = total // 10

            node.next = ListNode(total % 10)
            node = node.next

            tail = tail.next

        if carry:
            node.next = ListNode(carry)

        return head.next
