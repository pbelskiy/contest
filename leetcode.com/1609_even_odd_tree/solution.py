class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, 0)])
        while q:
            nq = deque()
            prev = None
            while q:
                node, level = q.popleft()

                if node.val % 2 == level % 2:
                    return False

                if prev is not None:
                    if node.val == prev:
                        return False

                    if level % 2 == 0:
                        if node.val < prev:
                            return False
                    else:
                        if node.val > prev:
                            return False

                prev = node.val

                if node.left:
                    nq.append((node.left, level + 1))
                if node.right:
                    nq.append((node.right, level + 1))

            q = nq

        return True
