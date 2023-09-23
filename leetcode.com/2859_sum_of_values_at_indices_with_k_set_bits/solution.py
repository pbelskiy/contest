class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        return sum(nums[i] for i in range(len(nums)) if i.bit_count() == k)
