class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zp = 0
        while zp < len(nums) - 1 and nums[zp] != 0:
            zp += 1

        for i, v in enumerate(nums):
            if v != 0 and zp < i:
                nums[zp], nums[i] = nums[i], nums[zp]
                zp += 1
