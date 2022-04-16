class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        @functools.cache
        def dfs(i, j):
            if j == len(key):
                return 0

            steps = []

            for k in range(len(ring)):
                if ring[k] == key[j]:
                    d = min(abs(i - k), len(ring) - abs(i - k))
                    steps.append(1 + d + dfs(k, j + 1))

            return min(steps)

        return dfs(0, 0)
