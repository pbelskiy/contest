class Solution:

    @staticmethod
    def convert(s):
        ns = ''
        value = s[0]
        total = 1

        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                total += 1
            else:
                ns += str(total) + value
                value = s[i]
                total = 1

        ns += str(total) + value
        return ns

    def countAndSay(self, n: int) -> str:
        if n <= 1:
            return '1'

        return self.convert(self.countAndSay(n - 1))
