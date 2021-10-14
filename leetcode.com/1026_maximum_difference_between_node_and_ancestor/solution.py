class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs(node, maximum, minimum):
            if not node:
                return abs(maximum - minimum)

            maximum = max(maximum, node.val)
            minimum = min(minimum, node.val)

            return max(dfs(node.left, maximum, minimum), dfs(node.right, maximum, minimum))

        return dfs(root, root.val, root.val)
