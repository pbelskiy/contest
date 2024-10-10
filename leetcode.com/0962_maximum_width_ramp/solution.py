"""
Maintain monothinic decreasing stack and for each new
element try to find better candidate in stack.

TC: O(N^2)
SC: O(N)
"""
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        best = 0
        stack = []

        for i, n in enumerate(nums):

            # maintain monothinic decreasing stack
            if not stack or stack[-1][0] > n:
                stack.append((n, i))

            # find closest value for current pair
            # (to boost performance we can use binary search here)
            for j in range(len(stack) - 1, -1, -1):
                if stack[j][0] > n:
                    break

                best = max(best, i - stack[j][1])

        return best
