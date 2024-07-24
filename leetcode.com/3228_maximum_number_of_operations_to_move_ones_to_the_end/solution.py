class Solution:
    def maxOperations(self, s: str) -> int:
        t = 0
        k = 0

        i = 0
        while True:

            while i < len(s) and s[i] == '1':
                i += 1
                k += 1

            if i == len(s):
                break

            while i < len(s) and s[i] == '0':
                i += 1

            t += k

        return t
