"""
Calculate manually

TC: O(N)
SC: O(N)
"""
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        r = abs(numerator)
        d = abs(denominator)

        full, r = divmod(r, d)

        seen = set()
        fraction = []

        while True:
            n, r = divmod(r*10, d)

            if (n, r) in seen:
                break

            fraction.append((n, r))
            seen.add((n, r))

        if n == 0 and r == 0:
            fraction = fraction[:-1]
        else:
            fraction.insert(fraction.index((n, r)), ('(', None))
            fraction.append((')', None))

        fr = ''.join(map(str, [n for n, _ in fraction]))

        sign = ''
        if numerator < 0 and denominator < 0:
            sign = ''
        elif numerator != 0 and (numerator < 0 or denominator < 0):
            sign = '-'

        res = f'{sign}{full}'
        if fr:
            res += f'.{fr}'

        return res

