class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node, d, w):
            if not node:
                return

            levels[d].append(w)
            dfs(node.left, d + 1, w*2)
            dfs(node.right, d + 1, w*2 + 1)

        levels = collections.defaultdict(list)
        dfs(root, 0, 0)

        best = 1
        for v in levels.values():
            if len(v) <= 1:
                continue
            best = max(best, max(v) - min(v) + 1)

        return best
