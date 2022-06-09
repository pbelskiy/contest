class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(node, total):
            if not node:
                return 0
            total += node.val
            return int(total == targetSum) + dfs(node.left, total) + dfs(node.right, total)

        def trace(node):
            if not node:
                return 0
            return trace(node.left) + trace(node.right) + dfs(node, 0)

        return trace(root)
