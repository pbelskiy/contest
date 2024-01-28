class Solution:
    def maximumLength(self, nums: List[int]) -> int:

        @cache
        def dfs(n):
            s = int(math.sqrt(n))
            if s == n or s**2 != n or count[s] < 2:
                return 0
            return dfs(s) + 2

        count = Counter(nums)
        m = max(1, count[1])
        if m % 2 == 0:
            m -= 1

        for n in nums:
            m = max(m, dfs(n) + 1)

        return m
