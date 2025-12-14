class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        return abs(sum(sorted(nums)[-k:]) - sum(sorted(nums)[:k]))

