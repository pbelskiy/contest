class Solution:

    def dfs(self, node, depth):
        if not node:
            return depth

        return max(self.dfs(node.left, depth + 1), self.dfs(node.right, depth + 1))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
