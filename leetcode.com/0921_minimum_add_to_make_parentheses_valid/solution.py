class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for p in s:
            if p == '(':
                stack.append(p)
            elif stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(p)

        return len(stack)
