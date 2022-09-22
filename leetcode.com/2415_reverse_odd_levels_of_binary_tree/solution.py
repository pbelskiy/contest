class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node, level):
            if not node:
                return

            if level % 2 == 1:
                levels[level].append(node)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        levels = defaultdict(list)
        dfs(root, 0)

        for nodes in levels.values():
            for i in range(len(nodes) // 2):
                nodes[i].val, nodes[len(nodes) - i - 1].val = nodes[len(nodes) - i - 1].val, nodes[i].val

        return root
