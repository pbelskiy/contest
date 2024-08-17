class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]

        ranges = []

        if lower < nums[0]:
            ranges.append([lower, nums[0] - 1])

        for i in range(len(nums) - 1):
            if nums[i] + 1 != nums[i + 1]:
                ranges.append([
                    nums[i] + 1,
                    nums[i + 1] - 1
                ])

        if upper > nums[-1]:
            ranges.append([nums[-1] + 1, upper])

        return ranges
