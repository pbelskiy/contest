class Solution:

    def prune(self, node):
        if node.left and self.prune(node.left):
            node.left = None

        if node.right and self.prune(node.right):
            node.right = None

        return node.val == 0 and node.left is node.right is None

    def pruneTree(self, root: TreeNode) -> TreeNode:
        if self.prune(root):
            return None
        return root
