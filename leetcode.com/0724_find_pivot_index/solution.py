class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)

        for i in range(len(nums)):
            left += nums[i]

            if left == right:
                return i

            right -= nums[i]

        return -1
