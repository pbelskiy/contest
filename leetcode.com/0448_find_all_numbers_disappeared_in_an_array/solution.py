class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return set(range(1, max(max(nums), len(nums)) + 1)) - set(nums)
