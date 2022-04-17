class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = 1

        for n in nums:
            p *= n

        if p == 0:
            return 0

        return -1 if p < 0 else 1
