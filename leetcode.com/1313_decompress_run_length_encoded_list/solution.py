class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        r = []

        for i in range(0, len(nums) - 1, 2):
            r.extend([nums[i + 1] for _ in range(nums[i])])

        return r
