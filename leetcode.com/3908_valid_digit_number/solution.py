class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        if str(n).startswith(str(x)):
            return False
        
        return str(x) in str(n)

