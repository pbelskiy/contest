"""
Erase all `[]` then string become like `][` or `]]][[[`

Then calculate number of swaps needed.

TC: O(N)
SC: O(N)
"""
class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []

        # fold all `[]` occurrences
        for ch in s:
            if stack and stack[-1] == '[' and ch == ']':
                stack.pop()
            else:
                stack.append(ch)

        # calculate number of operations
        return (len(stack) // 2 + 1) // 2
