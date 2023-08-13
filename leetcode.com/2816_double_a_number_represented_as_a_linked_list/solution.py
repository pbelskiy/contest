class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        digits = []
        node = head
        while node:
            digits.append(str(node.val))
            node = node.next

        sys.set_int_max_str_digits(20000)
        number = str(int(''.join(digits))*2)

        node = head = ListNode()
        for d in number:
            node.next = ListNode(d)
            node = node.next

        return head.next
