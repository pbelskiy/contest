"""
Due to array is sorted, we can use brute force.

TC: O(N^2)
SC: O(N)
"""
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:

        def dfs(i, j):
            x = arr[i] + arr[j]
            if x in d:
                return dfs(j, d[x]) + 1

            return 0

        m = 0
        d = {}

        for i, n in enumerate(arr):
            d[n] = i

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if v := dfs(i, j):
                    m = max(m, v + 2)

        return m
