class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = 0

        for n in nums:
            d ^= n
            print(bin(d))

        return d