# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.paths = []

    def solve(self, node, path):
        if not node:
            return

        if node.left:
            self.solve(node.left, [*path, node.val])
        elif node.right == None:
            self.paths.append([*path, node.val])

        if node.right:
            self.solve(node.right, [*path, node.val])
        elif node.left == None:
            self.paths.append([*path, node.val])

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.solve(root, [])

        r = []

        for p in self.paths:
            s = '->'.join(map(str, p))
            if s not in r:
                r.append(s)

        return r
