class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        s, d = 0, 0
    
        for x in str(n):
            s += int(x)**2
            d += int(x)

        return s - d >= 50

