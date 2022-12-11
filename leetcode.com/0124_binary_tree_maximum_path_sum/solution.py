class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return float('-inf')

            left = dfs(node.left)
            right = dfs(node.right)

            self.best = max(
                self.best,
                node.val,
                left,
                right,
                node.val + left,
                node.val + right,
                node.val + left + right
            )

            return max(
                node.val,
                node.val + left,
                node.val + right,
            )

        self.best = float('-inf')
        return max(dfs(root), self.best)
