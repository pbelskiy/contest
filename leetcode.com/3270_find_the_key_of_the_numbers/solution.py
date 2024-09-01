class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        n1 = str(num1).rjust(4, '0')
        n2 = str(num2).rjust(4, '0')
        n3 = str(num3).rjust(4, '0')

        key = ''

        for a, b, c in zip(n1, n2, n3):
            key += min(a, b, c)

        return int(key)
