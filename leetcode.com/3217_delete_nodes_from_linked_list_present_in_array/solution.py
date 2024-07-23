class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)

        head = ListNode(next=head)
        node = head
        while node:
            if node.next and node.next.val in s:
                node.next = node.next.next
            else:
                node = node.next

        return head.next
