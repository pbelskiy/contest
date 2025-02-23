class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            ss = ''

            for i in range(len(s) - 1):
                ss += str(((int(s[i]) + int(s[i + 1])) % 10))

            s = ss

        return len(set(s)) == 1
