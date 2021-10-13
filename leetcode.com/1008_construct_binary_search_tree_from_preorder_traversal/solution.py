class Solution:
    def bst_append(self, node, value):
        while node:
            if value > node.val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(value)
                    return
            else:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(value)
                    return

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])

        for n in preorder[1:]:
            self.bst_append(root, n)

        return root
