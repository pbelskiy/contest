class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def build(node):
            if not node:
                return

            return TreeNode(node.val, build(node.right), build(node.left))

        return build(root)
