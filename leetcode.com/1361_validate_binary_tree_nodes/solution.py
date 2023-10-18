class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # get list of possible start roots
        g = defaultdict(list)
        nodes = set(range(n))
        for i in range(n):
            if leftChild[i] != -1:
                g[i].append(leftChild[i])
                nodes.discard(leftChild[i])

            if rightChild[i] != -1:
                g[i].append(rightChild[i])
                nodes.discard(rightChild[i])

        # only one root can be in valid binary tree
        if len(nodes) != 1:
            return False

        # check that every node from root visited only once
        root = next(iter(nodes))
        q = deque([root])
        v = set([root])

        while q:
            i = q.popleft()

            if leftChild[i] in v:
                return False
            if leftChild[i] != -1:
                q.append(leftChild[i])
                v.add(leftChild[i])

            if rightChild[i] in v:
                return False
            if rightChild[i] != -1:
                q.append(rightChild[i])
                v.add(rightChild[i])

        return len(v) == n
