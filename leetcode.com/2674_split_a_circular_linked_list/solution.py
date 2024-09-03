class Solution:
    def splitCircularLinkedList(self, root: Optional[ListNode]) -> List[Optional[ListNode]]:
        node = root.next
        size = 1

        while node != root:
            node = node.next
            size += 1

        size_first = ceil(size / 2)
        size_second = size - size_first

        # split first
        node = root
        for _ in range(size_first - 1):
            node = node.next

        root_2 = node.next
        node.next = root

        # split second
        node = root_2
        for _ in range(size_second - 1):
            node = node.next

        node.next = root_2

        return [root, root_2]
