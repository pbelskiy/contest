class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        @cache
        def get_max(i, j):
            return max(jobDifficulty[i:j])

        @cache
        def solve(i, r):
            if r == 0:
                return 0 if i == n else float('inf')

            best = float('inf')
            for j in range(i + 1, n + 1):
                best = min(best, get_max(i, j) + solve(j, r - 1))

            return best

        n = len(jobDifficulty)
        if n < d:
            return -1

        v = solve(0, d)
        return v if v != float('inf') else -1
