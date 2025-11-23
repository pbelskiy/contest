class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        def is_possible(m, right):
            i = bisect.bisect(nums, m, hi=right) - 1
            if i == -1:
                return False

            if i >= 0 and nums[i] == m:
                return True

            if nums[i] > m:
                return False

            return is_possible(m - nums[i], i)

        nums.sort()
        t = sum(nums)
        m = t % 3

        while m > 0 and m <= t:
            if is_possible(m, len(nums)):
                return t - m

            m += 3

        return t

