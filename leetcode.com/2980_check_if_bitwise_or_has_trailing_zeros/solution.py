class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        t = 0

        for n in nums:
            if n & 1 == 0:
                t += 1

            if t >= 2:
                return True

        return False
