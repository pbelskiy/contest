class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)

        vals = []
        dfs(root)

        d = float('inf')
        m = float('inf')

        for v in sorted(vals):
            if abs(target - v) < d:
                d = abs(target - v)
                m = v

        return m
