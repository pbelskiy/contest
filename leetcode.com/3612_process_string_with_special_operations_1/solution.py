class Solution:
    def processStr(self, s: str) -> str:
        result = ''

        for ch in s:
            if ch == '*':
                if result:
                    result = result[:-1]
            elif ch == '#':
                result *= 2
            elif ch == '%':
                result = result[::-1]
            else:
                result += ch

        return result

