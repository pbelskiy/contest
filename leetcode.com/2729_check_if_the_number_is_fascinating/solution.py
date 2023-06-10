class Solution:
    def isFascinating(self, n: int) -> bool:
        s = str(n) + str(n*2) + str(n*3)
        return len(s) == len(set(s)) == 9 and '0' not in s
