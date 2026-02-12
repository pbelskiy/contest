class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        t = 1

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] <= nums[i - 1]:
                break
            t += 1

        return len(nums) - t

