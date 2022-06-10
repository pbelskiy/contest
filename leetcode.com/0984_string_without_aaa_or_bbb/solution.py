class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        t = a + b
        s = ''

        while a + b > 0:

            if s[-2:] == 'aa':
                s += 'b'
                b -= 1
            if s[-2:] == 'bb':
                s += 'a'
                a -= 1

            elif a > b:
                s += 'a'
                a -= 1
            else:
                s += 'b'
                b -= 1

        # print(s, len(s) == t and 'aaa' not in s and 'bbb' not in s, s.count('a'), s.count('b'))
        return s
