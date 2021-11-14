class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        length = 1
        node = head
        while node.next:
            node = node.next
            length += 1
        node.next = head

        i = length - (k % length) - 1
        node = head
        while i > 0 and node:
            node = node.next
            i -= 1

        head = node.next
        node.next = None
        return head
