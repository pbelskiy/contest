class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:

        def dfs(node, d):
            if not node:
                return

            if node is u:
                self.t = d

            v[d].append(node)
            dfs(node.left, d + 1)
            dfs(node.right, d + 1)

        v = defaultdict(list)
        dfs(root, 0)

        if v[self.t][-1].val == u.val:
            return None

        for i in range(len(v[self.t])):
            if v[self.t][i] is u:
                return v[self.t][i + 1]
