class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        levels = collections.defaultdict(int)

        def dfs(node, level):
            if node.left:
                dfs(node.left, level + 1)

            if node.right:
                dfs(node.right, level + 1)

            if node.left is node.right is None:
                levels[level] += node.val

        dfs(root, 0)
        return levels[max(levels.keys())]
