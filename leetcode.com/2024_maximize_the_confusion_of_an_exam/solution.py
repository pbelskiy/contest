"""
Get maximum from two sliding window of different targets.

TC: O(N)
SC: O(1)
"""

class Solution:
    def maxConsecutiveAnswers(self, a: str, k: int) -> int:

        def sliding_window(t, k):
            longest = 0
            left = 0

            for right in range(len(a)):
                # decrease possible changes counter
                if a[right] == t:
                    k -= 1

                # update max when we in balance
                if k >= 0:
                    longest = max(longest, right - left + 1)
                    continue

                # update balance of possible changes
                while k != 0:
                    if a[left] == t:
                        k += 1
                    left += 1

            return longest

        return max(sliding_window('T', k), sliding_window('F', k))
