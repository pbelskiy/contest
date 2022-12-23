"""
1) Initially I wrote naive BFS from each node and it took O(N^2) and abvoiusly
   gives us TLE, with result: `64 / 73 test cases passed.`

2) Then I tried DFS + cache which always helps in DP problems, but functions
   signature was `dfs(node, parent, depth)` so there were many cache misses and
   also gives TLE, but with result as `70 / 73 test cases passed.`

3) So, finally I figure out that some how need to reduce arguments in DFS function,
   and `depth` argument can be replaced just by calculation and returning tuple of
   `count` and `total` from function, and on each return we just sum up it.

Thanks to @choiking10 with his DFS without `depth` argument.
https://leetcode.com/problems/sum-of-distances-in-tree/discuss/2939374/Python-Super-Simple-O(N)-DP-Solution
"""

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:

        @cache
        def dfs(i, p):
            total = 0
            count = 1

            for j in g[i]:
                if j == p:  # don't go back it's tree!
                    continue

                t, c = dfs(j, i)

                # here magic with `depth`, every time
                # we return from deep call, we just multiply count
                # it give us correct distance as result
                total += t + c
                count += c

            return total, count

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        return [dfs(i, -1)[0] for i in range(n)]
