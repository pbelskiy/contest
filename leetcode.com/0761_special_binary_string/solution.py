class Solution:
    def makeLargestSpecial(self, s: str) -> str:

        def solve(s):
            p = []
            b = 0
            ss = ''
            for ch in s:
                if ch == '1':
                    b += 1
                else:
                    b -= 1
                ss += ch

                if b == 0:
                    p.append(ss)
                    ss = ''

            # only one big block
            if len(p) == 1:
                return '1' + solve(s[1:-1]) + '0'

            return ''.join(sorted([solve(pp) for pp in p], reverse=True))

        return solve(s)

