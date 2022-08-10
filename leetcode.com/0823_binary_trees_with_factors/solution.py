class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:

        def get_factors(v):
            for a in ars:
                b = v // a
                if v % a == 0 and b in ars:
                    yield a, b

        @cache
        def dfs(n):
            total = 1
            for a, b in get_factors(n):
                total += dfs(a) * dfs(b)
            return total

        ars = set(arr)
        arr.sort()
        return sum(map(dfs, arr)) % (10**9 + 7)
