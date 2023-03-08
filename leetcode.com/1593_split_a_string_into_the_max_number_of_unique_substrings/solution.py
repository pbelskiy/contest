class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        def solve(i, v):
            if i == len(s):
                return 0

            m = 0
            for j in range(i, len(s)):
                ss = s[i:j+1]
                if ss not in v:
                    m = max(m, solve(j + 1, v[:] + [ss]) + 1)

            return m

        return solve(0, [])
