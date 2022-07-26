class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs1(node, target):
            if not node:
                return False

            if node.val == target.val:
                return True

            return dfs1(node.left, target) or dfs1(node.right, target)

        def dfs2(node):
            if self.node or node == p or node == q:
                return True

            if not node:
                return False

            left, right = dfs2(node.left), dfs2(node.right)

            if left and right and not self.node:
                self.node = node

            return left or right

        if dfs1(p, q):
            return p
        if dfs1(q, p):
            return q

        self.node = None
        dfs2(root)
        return self.node
