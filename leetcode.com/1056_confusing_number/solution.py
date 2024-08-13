class Solution:
    def confusingNumber(self, n: int) -> bool:
        s = str(n)
        ns = ''
        for ch in reversed(s):
            if ch == '0':
                ns += '0'
            elif ch == '1':
                ns += '1'
            elif ch == '6':
                ns += '9'
            elif ch == '8':
                ns += '8'
            elif ch == '9':
                ns += '6'
            else:
                return False

        return int(ns) != n
