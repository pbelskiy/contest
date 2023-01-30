class Solution:
    def solveEquation(self, s: str) -> str:
        left, right = 0, 0
        mid = False
        sign = 1

        i = 0
        while i < len(s):

            if s[i] == '-':
                sign = -1
            elif s[i] == '+':
                sign = 1
            elif s[i] == '=':
                sign = 1
                mid = True

            # parse number
            d = ''
            while i < len(s) and s[i].isdigit():
                d += s[i]
                i += 1

            # parse x
            if i < len(s) and s[i] == 'x':
                if d:
                    v = int(d)
                else:
                    v = 1

                if mid:
                    left -= v*sign
                else:
                    left += v*sign

            elif d:
                if mid:
                    right += int(d)*sign
                else:
                    right -= int(d)*sign

                i -= 1

            i += 1

        if left == 0 and right == 0:
            return 'Infinite solutions'

        if left == 0:
            return 'No solution'

        return f'x={right // left}'
