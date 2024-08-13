class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:

        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)

        vals = []
        dfs(root)

        diff = sorted([([abs(target - v), v]) for v in vals])
        return [v for _, v in diff[:k]]
