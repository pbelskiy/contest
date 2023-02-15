class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        left = 0
        op = 0
        res = ''

        for i, ch in enumerate(s):
            if ch == '(':
                op += 1
            else:
                op -= 1

            if op == 0:
                res += s[left+1:i]
                left = i + 1

        return res
