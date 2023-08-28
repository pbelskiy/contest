class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'

        s = []
        d = abs(num)
        while d:
            d, m = divmod(d, 7)
            s += str(m)

        sign = '' if num >= 0 else '-'
        return sign + ''.join(reversed(s))
