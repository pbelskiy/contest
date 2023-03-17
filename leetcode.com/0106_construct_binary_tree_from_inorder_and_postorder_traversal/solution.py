"""
Traverse types:
    pre  order: root -> left -> right
    in   order: left -> root -> right
    post order: left -> right -> root

So here last value of postorder is root, and left and right
side of inorder index is corresponding subtrees.
"""
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def build(a):
            if not a:
                return

            val = postorder[self.last]
            node = TreeNode(val)
            self.last -= 1
            if not a:
                return node

            mid = a.index(val)
            node.right = build(a[mid+1:])
            node.left = build(a[:mid])
            return node

        self.last = len(postorder) - 1
        return build(inorder)
