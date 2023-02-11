class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def build(values):
            if not values:
                return

            mid = len(values) // 2

            node = TreeNode(values[mid])
            node.left = build(values[:mid])
            node.right = build(values[mid+1:])
            return node

        values = []
        while head:
            values.append(head.val)
            head = head.next

        return build(values)
