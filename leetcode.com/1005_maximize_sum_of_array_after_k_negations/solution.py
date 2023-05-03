class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        for i in range(len(nums)):
            if nums[i] >= 0:
                break

            nums[i] = -nums[i]
            k -= 1

            if k == 0:
                break

        if k > 0 and k % 2 == 1:
            return sum(nums) - min(nums)*2

        return sum(nums)
