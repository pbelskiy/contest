import queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        r_val, r_depth = None, -1

        q = queue.Queue()
        q.put((root, 0, True))

        while not q.empty():
            node, depth, left = q.get()

            if left and depth > r_depth:
                r_val, r_depth = node.val, depth

            if node.left:
                q.put((node.left, depth + 1, True))

            if node.right:
                q.put((node.right, depth + 1, node.left is None))

        return r_val


# [3,1,5,0,2,4,6]
# [0,null,-1]
# [1]
# [2,1,3]
# [1,2,3,4,null,5,6,null,null,7]
