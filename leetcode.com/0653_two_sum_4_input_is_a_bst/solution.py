class Solution:
    def dfs(self, node):
        if not node:
            return

        self.nums.append(node.val)
        self.dfs(node.left)
        self.dfs(node.right)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.nums = []
        self.dfs(root)
        deltas = set()

        for n in self.nums:
            if n in deltas:
                return True
            deltas.add(k - n)

        return False
