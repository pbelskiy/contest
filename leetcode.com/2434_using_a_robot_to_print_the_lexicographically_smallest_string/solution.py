"""
Logically we should consume `s` to stack until no better character
in future.

To reduce TC we use Counter to check characters ahead.

TC: O(N)
SC: O(N)
"""
class Solution:
    def robotWithString(self, s: str) -> str:
        count = Counter(s)
        stack = []
        t = ''

        for i, ch in enumerate(s):
            # if no better character in fututre, then pop
            while stack and stack[-1] <= min(count):
                t += stack.pop()

            stack.append(ch)

            count[ch] -= 1
            if count[ch] <= 0:
                del count[ch]

        return t + ''.join(reversed(stack))
