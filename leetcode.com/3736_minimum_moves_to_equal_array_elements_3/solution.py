class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(max(nums) - n for n in nums)

