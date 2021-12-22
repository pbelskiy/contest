class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def get_depth(node):
            if not node:
                return 0

            return max(get_depth(node.left), get_depth(node.right)) + 1

        if not root:
            return True

        return (abs(get_depth(root.left) - get_depth(root.right)) < 2) and \
                self.isBalanced(root.left) and self.isBalanced(root.right)
