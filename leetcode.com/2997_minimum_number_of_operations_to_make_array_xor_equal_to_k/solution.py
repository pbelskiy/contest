class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x = 0
        for n in nums:
            x ^= n

        # count number of diff in bit positions
        t = 0
        for i in range(32):
            if (x & (1 << i)) != (k & (1 << i)):
                t += 1

        return t
