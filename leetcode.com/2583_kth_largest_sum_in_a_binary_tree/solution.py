class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node, d):
            if not node:
                return
            levels[d] += node.val
            dfs(node.left, d + 1)
            dfs(node.right, d + 1)

        levels = defaultdict(int)
        dfs(root, 0)
        if k > len(levels):
            return -1
        return sorted(levels.values())[-k]
