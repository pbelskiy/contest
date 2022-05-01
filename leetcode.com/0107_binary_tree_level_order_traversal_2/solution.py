class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        def dfs(node, level):
            if not node:
                return

            levels[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        levels = collections.defaultdict(list)
        dfs(root, 0)
        return reversed(levels.values())
