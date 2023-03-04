"""
Naive approach, we could see that is just +4 new block on each step.

brute force solution is O(N):
    return 1 + 4*sum(range(n))

But it's easy to translate it to O(1):
    return 1 + 4*(n*(n - 1) // 2)

https://en.wikipedia.org/wiki/Arithmetic_progression
"""

class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 4*(n*(n - 1) // 2)
