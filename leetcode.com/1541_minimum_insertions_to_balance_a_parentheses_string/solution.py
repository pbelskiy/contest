class Solution:
    def minInsertions(self, s: str) -> int:
        i, n, o = 0, 0, 0

        while i < len(s):
            if s[i] == '(':
                o += 1

            elif i + 1 < len(s) and s[i + 1] == ')':

                if o > 0:
                    o -= 1
                else:
                    n += 1  # missed `(`

                i += 1

            else:

                if o > 0:
                    o -= 1
                    n += 1  # missed `)`
                else:
                    n += 2

            i += 1

        return n + o*2
