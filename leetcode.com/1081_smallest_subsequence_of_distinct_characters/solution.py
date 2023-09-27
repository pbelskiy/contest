class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []

        for i, ch in enumerate(s):
            if ch in stack:
                continue

            while stack and ch < stack[-1] and stack[-1] in s[i:]:
                stack.pop()
            stack.append(ch)

        return ''.join(stack)
