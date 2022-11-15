class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return
            values.append(node.val)
            dfs(node.left)
            dfs(node.right)

        values = []
        dfs(root)
        values.sort()
        return min(abs(values[i] - values[i + 1]) for i in range(len(values) - 1))
