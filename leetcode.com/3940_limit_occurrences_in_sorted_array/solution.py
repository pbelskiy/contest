class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        f = Counter()
        a = []

        for n in nums:
            if f[n] < k:
                f[n] += 1
                a.append(n)

        return a

