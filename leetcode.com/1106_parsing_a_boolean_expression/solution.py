
class Solution:

    def parse_or(self, p):
        print('|', p - 2)
        v = False

        while self.expression[p] != ')':
            if self.expression[p] == 'f':
                v |= False

            elif self.expression[p] == 't':
                v |= True

            elif self.expression[p] == '|':
                nv, np = self.parse_or(p + 2)
                v |= nv
                p = np
                continue

            elif self.expression[p] == '&':
                nv, np = self.parse_and(p + 2)
                v |= nv
                p = np
                continue

            elif self.expression[p] == '!':
                nv, np = self.parse_not(p + 2)
                v |= nv
                p = np
                continue

            p += 1

        return v, p + 1

    def parse_and(self, p):
        print('&', p - 2)
        v = True

        while self.expression[p] != ')':
            if self.expression[p] == 'f':
                v &= False

            elif self.expression[p] == 't':
                v &= True

            elif self.expression[p] == '|':
                nv, np = self.parse_or(p + 2)
                v &= nv
                p = np
                continue

            elif self.expression[p] == '&':
                nv, np = self.parse_and(p + 2)
                v &= nv
                p = np
                continue

            elif self.expression[p] == '!':
                nv, np = self.parse_not(p + 2)
                v &= nv
                p = np
                continue

            p += 1

        return v, p + 1

    def parse_not(self, p):
        print('!', p - 2)
        v = None

        while self.expression[p] != ')':
            if self.expression[p] == 'f':
                v = False

            elif self.expression[p] == 't':
                v = True

            elif self.expression[p] == '|':
                v, p = self.parse_or(p + 2)
                continue

            elif self.expression[p] == '&':
                v, p = self.parse_and(p + 2)
                continue

            elif self.expression[p] == '!':
                v, p = self.parse_not(p + 2)
                continue

            p += 1

        return not v, p + 1

    def parseBoolExpr(self, expression: str) -> bool:
        self.expression = expression

        if expression[0] == '|':
            v, _ = self.parse_or(2)

        elif expression[0] == '&':
            v, _ = self.parse_and(2)

        elif expression[0] == '!':
            v, _ = self.parse_not(2)

        return v


"""
"!(f)"
"|(f,t)"
"&(t,f)"
"|(&(t,f,t),!(t))"
"""

tc = "!(&(&(!(&(f)),&(t),|(f,f,t)),&(t),&(t,t,f)))"
print(Solution().parseBoolExpr(tc), '==', True)
