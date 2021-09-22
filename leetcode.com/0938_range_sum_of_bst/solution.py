class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        q = collections.deque([root])

        while q:
            node = q.popleft()

            if not node:
                continue

            if low <= node.val <= high:
                total += node.val

            q.append(node.left)
            q.append(node.right)

        return total
