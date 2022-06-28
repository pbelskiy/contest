class UnionFind:

    def __init__(self, n):
        self.p = list(range(n + 1))
        self.count = n

    def find(self, x):
        if self.p[x] == x:
            return x

        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        self.p[x] = y
        self.count -= 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for a, b in edges:
            uf.union(a, b)

        d = Counter()

        for i in range(n):
            d[uf.find(i)] += 1

        a = sorted(d.values())
        s = 0

        for v in a:
            s += (n - v) * v
            n -= v

        return s
