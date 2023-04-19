class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        @cache
        def dfs(node, b):
            if not node:
                return 0

            if b and node.left:
                return dfs(node.left, False) + 1
            elif not b and node.right:
                return dfs(node.right, True) + 1

            return 0

        nodes = []

        def collect(node):
            if node:
                nodes.append(node)
                collect(node.left)
                collect(node.right)

        collect(root)

        m = 0
        for node in nodes:
            m = max(m, dfs(node, False), dfs(node, True))

        return m
