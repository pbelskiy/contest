class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = list(s)
        stack = []

        for i, char in enumerate(chars):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    chars[i] = ''

        # erase extra braces
        while stack:
            chars[stack.pop()] = ''

        return ''.join(chars)
