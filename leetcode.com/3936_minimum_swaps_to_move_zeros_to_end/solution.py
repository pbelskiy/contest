class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        total = 0

        while left < right:
            while left < right and nums[left] != 0:
                left += 1

            while right > left and nums[right] == 0:
                right -= 1

            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                total += 1

        return total

