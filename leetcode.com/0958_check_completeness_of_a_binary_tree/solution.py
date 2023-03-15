# TODO: solution could be much simpler
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        d = 0
        while q:
            nq = deque()
            count = 0
            not_next = False
            while q:
                n = q.popleft()
                count += 1

                if n.left:
                    nq.append(n.left)
                if n.right:
                    nq.append(n.right)

                if n.right and not n.left:
                    return False

                if not_next and (n.left or n.right):
                    return False

                if not n.left or not n.right:
                    not_next = True

            if count != 2**d and nq:
                return False

            d += 1
            q = nq

        return True
