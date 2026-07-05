class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        m = float('-inf')
        for n in nums:
            lo, hi = min(str(n)), max(str(n))
            dr = int(hi) - int(lo)
            m = max(m, dr)
        
        s = 0
        for n in nums:
            lo, hi = min(str(n)), max(str(n))
            dr = int(hi) - int(lo)
            if dr == m:
                s += n

        return s

