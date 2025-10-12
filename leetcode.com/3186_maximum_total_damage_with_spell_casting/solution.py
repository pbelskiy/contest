class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:

        @cache
        def dfs(i):
            if i >= len(a):
                return 0

            t = a[i] * count[a[i]]

            return max(
                dfs(bisect.bisect(a, a[i] + 2, lo=i)) + t,
                dfs(i + 1),
            )

        count = Counter(power)
        a = sorted(count)
        return max(dfs(i) for i in range(len(a)))

