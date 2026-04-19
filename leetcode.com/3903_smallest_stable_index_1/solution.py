class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(len(nums)):
            if max(nums[0:i+1]) - min(nums[i:n]) <= k:
                return i

        return -1

