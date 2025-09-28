class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        a = list(str(n))
        r = []

        for i in range(len(a) - 1, -1, -1):
            if a[i] == '0':
                continue

            r.append(int(''.join(a[i:])))
            a[i] = '0'

        return r[::-1]

