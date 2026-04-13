class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        t = 0
        for n in nums:
            t += str(n).count(str(digit))
        return t

