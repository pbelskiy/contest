class Solution:
    def findNumber(self) -> int:
        r = 0

        for i in range(30):
            if commonSetBits(1 << i):
                r |= 1 << i

        return r
