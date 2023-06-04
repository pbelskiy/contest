class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        ops = 0

        i = nums.index(len(nums))

        while i + 1 < len(nums):
            nums[i], nums[i+1] = nums[i+1], nums[i]
            i += 1
            ops += 1

        return ops + nums.index(1)
