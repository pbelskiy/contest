class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:

        def dfs(node):
            if not node:
                return

            nodes.append(node)
            dfs(node.left)
            dfs(node.right)

        if not root:
            return

        nodes = []
        dfs(root)

        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]

        nodes[-1].left = None
        nodes[-1].right = None
