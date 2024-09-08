class Solution:
    def convertDateToBinary(self, date: str) -> str:
        a, b, c = date.split('-')
        return bin(int(a))[2:] + '-' + bin(int(b))[2:] + '-' + bin(int(c))[2:]
