class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        s = 0
        m = 1

        left = 0
        for right in range(len(nums)):
            while nums[right] & s:
                s &= ~nums[left]
                left += 1

            s |= nums[right]
            m = max(m, right - left + 1)

        return m
