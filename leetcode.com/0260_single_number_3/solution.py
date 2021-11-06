class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # [1,2,1,3,2,5] as example, xor sum = 6

        # XORed two target numbers
        v1 = 0
        for n in nums:
            v1 ^= n

        # create mask to find all opposites, which
        # [1, 1, 5] -> unique by XOR = 5
        v2 = 0
        mask = v1 & -v1
        for n in nums:
            if n & mask == 0:
                v2 ^= n

        # return two targets
        return [v1 ^ v2, v2]
