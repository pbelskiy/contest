class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        a = []

        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                a.append(s)

        a.sort()
        t = 0

        for i in range(left, right + 1):
            t = (t + a[i - 1]) % (10**9 + 7)

        return t
