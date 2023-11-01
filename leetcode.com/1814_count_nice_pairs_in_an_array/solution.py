class Solution:
    def countNicePairs(self, nums: List[int]) -> int:

        @cache
        def rev(n):
            return int(str(n)[::-1])

        count = Counter()
        for n in nums:
            count[n - rev(n)] += 1

        total = 0
        for v in count.values():
            total = (total + (v*(v - 1)) // 2) % (10**9 + 7)

        return total
