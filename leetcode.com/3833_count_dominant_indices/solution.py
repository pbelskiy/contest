class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        t = 0

        for i in range(len(nums) - 1):
            if nums[i] > (sum(nums[i + 1:]) / len(nums[i + 1:])):
                t += 1

        return t

