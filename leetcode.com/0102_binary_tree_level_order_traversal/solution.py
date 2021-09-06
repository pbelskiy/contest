# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = []

        q = collections.deque()
        q.append(root)

        while q:
            l = []
            nq = collections.deque()

            while q:
                n = q.popleft()
                l.append(n.val)

                if n.left:
                    nq.append(n.left)
                if n.right:
                    nq.append(n.right)

            levels.append(l)
            q = nq

        return levels
