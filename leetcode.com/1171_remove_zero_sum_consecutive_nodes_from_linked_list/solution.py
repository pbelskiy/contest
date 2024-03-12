class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # convert to array
        a = []
        while head:
            a.append(head.val)
            head = head.next

        # trim array
        found = True
        while found:
            found = False
            for i in range(len(a)):
                s = 0
                j = i
                for j in range(i, len(a)):
                    s += a[j]
                    if s == 0:
                        break

                if s == 0:
                    found = True
                    a = a[:i] + a[j+1:]
                    break

        # convert to linked list
        if not a:
            return None

        head = node = ListNode()
        for n in a:
            node.next = ListNode(n)
            node = node.next

        return head.next
