class Solution:

    def trace(self, node, total, target, path):
        if node.left is node.right is None and total + node.val == target:
            self.pathes.append(path + [node.val])
            return

        if node.left:
            self.trace(node.left, total + node.val, target, path + [node.val])

        if node.right:
            self.trace(node.right, total + node.val, target, path + [node.val])

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []

        self.pathes = []
        self.trace(root, 0, targetSum, [])
        return self.pathes
