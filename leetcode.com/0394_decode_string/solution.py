class Solution:
    def decodeString(self, s: str) -> str:

        def trace(p):
            val = ''
            mul = ''

            while p < len(s):

                while p < len(s) and s[p].isdigit():
                    mul += s[p]
                    p += 1

                while p < len(s) and s[p].isalpha():
                    val += s[p]
                    p += 1

                if p >= len(s):
                    return val

                if s[p] == '[':
                    rv, p = trace(p + 1)

                    if mul:
                        val += int(mul) * rv
                        mul = ''
                    else:
                        val += rv

                elif s[p] == ']':
                    return val, p + 1

            return val

        return trace(0)
