class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        val, idx = max(nums), nums.index(max(nums))

        nums.pop(idx)
        if max(nums)*2 > val:
            return -1

        return idx
