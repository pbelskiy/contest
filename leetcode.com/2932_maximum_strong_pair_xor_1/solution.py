class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        best = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    best = max(best, nums[i] ^ nums[j])

        return best
