class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        indexes = []

        for i, n in enumerate(nums):
            if n == target:
                indexes.append(i)

        return indexes
