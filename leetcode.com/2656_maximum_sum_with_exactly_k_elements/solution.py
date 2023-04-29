class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return ((max(nums) + max(nums)+k-1)*k) // 2
