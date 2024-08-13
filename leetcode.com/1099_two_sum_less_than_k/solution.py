class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        m = -1

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < k:
                    m = max(m, nums[i] + nums[j])

        return m
