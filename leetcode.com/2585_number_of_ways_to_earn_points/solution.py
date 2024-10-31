class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:

        @cache
        def dfs(s, i):
            # target value is reached
            if s == target:
                return 1

            # out of types is reached
            if s > target or i >= len(types):
                return 0

            # skip mark
            t = dfs(s, i + 1)

            # try different sum of current mark
            for j in range(types[i][0]):
                t += dfs(s + types[i][1]*(j + 1), i + 1) % (10**9 + 7)

            return t % (10**9 + 7)

        return dfs(0, 0) % (10**9 + 7)
