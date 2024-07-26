class Solution:

    def get_changes(self, nums, n, k, x):
        t = 0
        for i in range(n // 2):
            d = abs(nums[i] - nums[n - i - 1])
            if d == x:
                continue

            a = nums[i]
            b = nums[n - i - 1]

            if 0 <= b + x <= k or 0 <= b - x <= k:
                t += 1
            elif 0 <= a + x <= k or 0 <= a - x <= k:
                t += 1
            else:
                t += 2

        return t

    def minChanges(self, a: List[int], k: int) -> int:
        n = len(a)

        # find X, the most common value
        values = [abs(a[i] - a[n - i - 1]) for i in range(n // 2)]

        m = float('inf')
        for x, _ in Counter(values).most_common()[:2]:
            m = min(m, self.get_changes(a, n, k, x))

        return m
