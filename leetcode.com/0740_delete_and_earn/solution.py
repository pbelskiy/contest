class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        @cache
        def dfs(i):
            if i == len(values):
                return 0

            m = 0
            for j in range(i, min(i + 2, len(values))):
                s = values[j] * count[values[j]]

                if j + 1 < len(values) and values[j] + 1 == values[j + 1]:
                    m = max(m, dfs(j + 2) + s)
                else:
                    m = max(m, dfs(j + 1) + s)

            return m

        count = Counter(nums)
        values = sorted(set(nums))
        return dfs(0)
