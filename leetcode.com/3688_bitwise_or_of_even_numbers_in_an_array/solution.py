class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        r = 0
        for n in nums:
            if n % 2 == 0:
                r |= n

        return r

