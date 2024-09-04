class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:

        def dfs(node, d):
            if not node:
                return
            l[d] += node.val
            dfs(node.left, d + 1)
            dfs(node.right, d + 1)

        l = defaultdict(int)
        dfs(root, 1)

        return sorted(l.items(), key=lambda t: t[1])[0][0]
