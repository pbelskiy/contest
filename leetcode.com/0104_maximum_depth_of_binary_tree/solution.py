class Solution:

    def dfs(self, node, depth):
        if not node:
            return depth

        return max(self.dfs(node.left, depth + 1), self.dfs(node.right, depth + 1))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)


# 16 Feb 2023
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node, d):
            if not node:
                return d
            return max(dfs(node.left, d + 1), dfs(node.right, d + 1))

        return dfs(root, 0)
