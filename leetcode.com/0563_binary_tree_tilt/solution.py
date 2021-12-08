class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return (0, 0)

            lt, ls = dfs(node.left)
            rt, rs = dfs(node.right)

            ct = abs(ls - rs)

            return (ct + lt + rt, node.val + ls + rs)

        return dfs(root)[0]
