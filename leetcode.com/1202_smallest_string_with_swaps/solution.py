class UnionFind:

    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x] == x:
            return x

        # path compression
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        self.p[x] = y


class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
        for a, b in pairs:
            uf.union(a, b)

        d = collections.defaultdict(list)
        for i in range(len(s)):
            d[uf.find(i)].append((i))

        # sort in unions
        a = list(s)
        for v in d.values():
            for i, j in zip(v, sorted(v, key=lambda i: s[i])):
                a[i] = s[j]

        return ''.join(a)
