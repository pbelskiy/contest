class Solution:
    def countElements(self, nums: List[int]) -> int:
        total = 0
        nums.sort()

        for i in range(len(nums)):
            if nums[0] < nums[i] < nums[-1]:
                total += 1

        return total
