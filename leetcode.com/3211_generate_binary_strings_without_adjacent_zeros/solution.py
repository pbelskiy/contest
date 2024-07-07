class Solution:
    def validStrings(self, n: int) -> List[str]:
        r = []

        for i in range(2**n):
            x = bin(i)[2:].rjust(n, '0')
            if '00' in x:
                continue
            r.append(x)

        return r
