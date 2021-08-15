class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        level = 0

        for ch in s:
            if ch == '(':
                level += 1
            elif ch == ')':
                level -= 1

            depth = max(depth, level)

        return depth
