class UnionFind:

    def __init__(self, n):
        self.p = list(range(n))

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        self.p[x] = y

    def find(self, x):
        if self.p[x] == x:
            return x

        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)
        equations.sort(key=lambda t: t[1] == '!')

        for eq in equations:
            x, y, e = ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a'), eq[1] == '='

            if e:
                uf.union(x, y)
            elif uf.connected(x, y):
                return False

        return True
