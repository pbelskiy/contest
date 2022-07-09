class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if node.left is node.right is None:
                return bool(node.val)

            # OR
            if node.val == 2:
                return dfs(node.left) or dfs(node.right)

            # AND
            return dfs(node.left) and dfs(node.right)

        return dfs(root)
