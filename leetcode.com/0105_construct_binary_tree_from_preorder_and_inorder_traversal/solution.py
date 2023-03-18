"""
pre  order: root -> left -> right
in   order: left -> root -> right
post order: left -> right -> root
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def build(a):
            if not a:
                return

            # root value of current subtree is always next index of preorder
            v = preorder[self.last]
            self.last += 1

            node = TreeNode(v)

            # left and right side of subtree is inorder parts
            i = a.index(v)
            node.left = build(a[:i])
            node.right = build(a[i+1:])
            return node

        self.last = 0
        return build(inorder)
