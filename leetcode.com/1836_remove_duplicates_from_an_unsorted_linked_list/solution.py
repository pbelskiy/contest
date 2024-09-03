class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        seen = set()
        target = set()

        # collect
        node = head
        while node:
            if node.val in seen:
                target.add(node.val)
            seen.add(node.val)
            node = node.next

        # remove
        node = head
        prev = node
        while node:
            if node.val not in target:
                prev = node
            elif node is head:
                head = node.next
            else:
                prev.next = node.next

            node = node.next

        return head
