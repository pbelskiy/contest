class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            if p.val != q.val:
                return False

            return all([self.isSameTree(p.left, q.left), self.isSameTree(p.right, q.right)])

        if bool(p) != bool(q):
            return False

        return True
