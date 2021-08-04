class Solution:

    def minDepth(self, root: TreeNode) -> int:
        m = 10**6

        def dfs(node, d):
            nonlocal m
            if node and node.left is node.right is None:
                m = min(m, d + 1)
                return

            if node.left:
                dfs(node.left, d + 1)
            if node.right:
                dfs(node.right, d + 1)


        if not root:
            return 0

        dfs(root, 0)
        return m
