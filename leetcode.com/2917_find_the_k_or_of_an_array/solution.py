class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        s = 0
        for i in range(max(nums).bit_length()):
            t = 0
            for n in nums:
                if n & (1 << i):
                    t += 1

            if t >= k:
                s += 2**i

        return s
