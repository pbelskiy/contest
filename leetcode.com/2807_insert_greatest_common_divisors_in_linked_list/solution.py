class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            a = curr.val
            b = curr.next.val
            d = gcd(a, b)

            temp = curr.next
            curr.next = ListNode(d, curr.next)
            curr = temp

        return head
