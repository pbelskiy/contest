class UnionFind:

    def __init__(self, n):
        self.p = list(range(n))

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)

    def find(self, x):
        if self.p[x] == x:
            return x

        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        uf = UnionFind(n)
        extra = 0
        count = n

        for x, y in connections:

            if uf.connected(x, y):
                extra += 1
            else:
                uf.union(x, y)
                count -= 1

        if count - 1 > extra:
            return -1

        return count - 1
