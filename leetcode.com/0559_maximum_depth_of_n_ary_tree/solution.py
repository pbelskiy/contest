class Solution:
    def maxDepth(self, root: 'Node') -> int:

        def dfs(node, level):
            if not node:
                return level

            nl = level
            for child in node.children:
                nl = max(nl, dfs(child, level + 1))

            return nl

        if not root:
            return 0

        return dfs(root, 1)
