"""
Group points by horizonal lines, then fast multiply
using prefix sum.

TC: O(N)
SC: O(N)
"""
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        g = defaultdict(int)
        for x, y in points:
            g[y] += 1

        # get total horizonal points by group and it's comb
        arr = list(g.values())
        for i in range(len(arr)):
            arr[i] = math.comb(arr[i], 2)

        # calc results
        t = 0
        before = 0
        for i in range(len(arr)):
            t = (t + arr[i] * before) % (10**9 + 7)
            before += arr[i]

        return t

