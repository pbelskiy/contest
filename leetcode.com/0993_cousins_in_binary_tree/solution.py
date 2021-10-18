class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        def dfs(node, parent, depth, target):
            if not node:
                return None

            if node.val == target:
                return (parent, depth)

            if r := dfs(node.left, node, depth + 1, target):
                return r
            if r:= dfs(node.right, node, depth + 1, target):
                return r

        px, dx = dfs(root, None, 0, x)
        py, dy = dfs(root, None, 0, y)

        if dx != dy:
            return False

        if px is py:
            return False

        return True
