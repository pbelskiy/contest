class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        i = 0
        while i < len(nums):

            j = i
            while j + 1 < len(nums) and nums[j] + 1 == nums[j + 1]:
                j += 1

            if nums[i] == nums[j]:
                ranges.append(str(nums[i]))
            else:
                ranges.append(f"{nums[i]}->{nums[j]}")

            i = j + 1

        return ranges
