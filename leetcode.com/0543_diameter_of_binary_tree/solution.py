class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node, n):
            if not node:
                return n

            l = dfs(node.left, n + 1)
            r = dfs(node.right, n + 1)

            self.best = max(self.best, (l - n - 1) + (r - n - 1))
            return max(l, r)

        self.best = 0
        dfs(root, 0)
        return self.best
