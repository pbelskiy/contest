class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        val = 0
        while left < right:
            val += int(str(nums[left]) + str(nums[right]))
            left += 1
            right -= 1

        if left == right:
            val += nums[left]

        return val
