class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def check(node1, node2):
            if node1 is None and node2 is None:
                return True

            if (node1 and not node2) or (not node1 and node2):
                return False

            if node1.val != node2.val:
                return False

            return check(node1.left, node2.left) and check(node1.right, node2.right)

        def dfs(node):
            if not node:
                return False

            if node.val == subRoot.val and check(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)

        return dfs(root)
