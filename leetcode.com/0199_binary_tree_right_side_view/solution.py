class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node, level):
            if not node:
                return

            levels[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        levels = defaultdict(list)
        dfs(root, 0)
        return [level[-1] for level in levels.values()]
