class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        a = [nums[0]]

        for i in range(1, len(nums) - 1):
            if max(nums[:i]) < nums[i] or nums[i] > max(nums[i + 1:]):
                a.append(nums[i])

        if len(nums) > 1:
            a.append(nums[-1])

        return a

