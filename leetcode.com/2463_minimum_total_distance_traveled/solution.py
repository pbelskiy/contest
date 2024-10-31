"""
Use simple recursion with cache. One trick here is
to flat factory into flat list of positions.

TC: O(NlgN)
SC: O(N)
"""
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:

        @cache
        def dfs(ri, fi):
            # all robots are assigned
            if ri == len(ra):
                return 0

            # all factories are consumed
            if fi == len(fa):
                return float('inf')

            # assign current robot to current factory
            pick = dfs(ri + 1, fi + 1) + abs(ra[ri] - fa[fi])

            # try next factory
            skip = dfs(ri, fi + 1)

            return min(pick, skip)

        ra = sorted(robot)
        fa = []

        # convert factory to flat list
        for f in sorted(factory):
            fa.extend([f[0]]*f[1])

        r = dfs(0, 0)
        dfs.cache_clear()  # due to GC, or need to use tabulation approach
        return r
