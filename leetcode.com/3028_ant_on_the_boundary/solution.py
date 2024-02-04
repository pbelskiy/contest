class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        t, b = 0, 0

        for n in nums:
            b += n
            if b == 0:
                t += 1

        return t
