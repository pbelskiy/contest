class Solution:
    def maximumGap(self, nums: List[int]) -> int:

        def radix_sort(a):
            base = 10
            ranks = len(str(max(a)))

            for r in range(ranks):
                buckets = [[] for _ in range(base)]
                for n in a:
                    idx = n // base**r % base
                    buckets[idx].append(n)

                a = [n for b in buckets for n in b]

            return a

        if len(nums) < 2:
            return 0

        a = radix_sort(nums)
        m = float("-inf")
        for i in range(len(a) - 1):
            m = max(m, a[i+1] - a[i])

        return m
