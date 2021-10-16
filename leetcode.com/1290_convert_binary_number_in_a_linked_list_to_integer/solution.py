class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        b = []

        while head:
            b.append(str(head.val))
            head = head.next

        return int('0b' + ''.join(b), 2)
