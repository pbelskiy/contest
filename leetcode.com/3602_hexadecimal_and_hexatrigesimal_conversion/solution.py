class Solution:
    def concatHex36(self, n: int) -> str:

        def to_base36(n):
            if n < 0:
                return '-' + to_base36(-n)

            if n == 0:
                return '0'

            s = ''

            while n:
                n, m = divmod(n, 36)
                s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[m] + s

            return s

        s1 = hex(n**2)[2:].upper()
        s2 = to_base36(n**3)

        return s1 + s2

