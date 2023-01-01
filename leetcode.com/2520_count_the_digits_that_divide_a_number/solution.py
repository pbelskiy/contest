class Solution:
    def countDigits(self, num: int) -> int:
        return len([d for d in str(num) if num % int(d) == 0])
