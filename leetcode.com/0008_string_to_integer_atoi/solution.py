class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. Read in and ignore any leading whitespace.
        s = s.lstrip()

        # 2. Check if the next character (if not already at the end of the string) is '-' or '+'.
        negative = True if len(s) > 0 and s[0] == '-' else False


        # 3.Read in next the characters until the next non-digit character or the end of the input is               # reached. The rest of the string is ignored.
        i = 1 if negative else 0

        if not negative and i < len(s) and s[i] == '+':
            i += 1

        ns = ''
        while i < len(s) and s[i].isdigit():
            ns += s[i]
            i += 1

        # 4. Convert these digits into an integer
        n = int(ns) if ns else 0

        if negative:
            n = -n

        # 5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the               # integer
        if n > 2**31 - 1:
            return 2**31 - 1

        if n < -2**31:
            return -2**31

        # 6. Return the integer as the final result.
        return n
