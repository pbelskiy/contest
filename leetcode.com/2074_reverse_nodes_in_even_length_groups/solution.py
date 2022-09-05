class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(first, count):
            if not (first and count % 2 == 0):
                return

            values = []
            begin = first

            while count:
                values.append(begin.val)
                begin = begin.next
                count -= 1

            j = len(values) - 1
            while first and j >= 0:
                first.val = values[j]
                first = first.next
                j -= 1

        first = head
        need = 1
        count = 0

        node = head
        while node:
            count += 1

            if count == need:
                reverse(first, count)
                need += 1
                count = 0
                first = node.next

            node = node.next

        reverse(first, count)
        return head
