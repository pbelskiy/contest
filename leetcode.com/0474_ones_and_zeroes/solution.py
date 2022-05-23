class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        @cache
        def dfs(i, a, b):
            if a < 0 or b < 0:
                return -1

            if i + 1 < len(strs):
                return max(
                    dfs(i + 1, a - zeros[i + 1], b - ones[i + 1]) + 1,
                    dfs(i + 1, a, b)
                )

            return 0

        strs.sort(key=len)
        zeros = [s.count("0") for s in strs]
        ones = [s.count("1") for s in strs]
        return dfs(-1, m, n)
