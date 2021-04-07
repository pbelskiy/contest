class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            v = int('-' + ''.join(reversed(str(x)[1:])))
        else:
            v = int(''.join(reversed(str(x))))

        if -2**31 < v < 2**31:
            return v

        return 0
