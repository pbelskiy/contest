"""
Use greedy solution here.

1) Earn points using minimal energy available
2) Get energy using largest possible energy

TC: O(NlogN)
SC: O(N)
"""
class Solution:
    def maximumPoints(self, a: List[int], e: int) -> int:
        a.sort(reverse=True)

        if e // a[-1] < 1:
            return 0

        points = 0

        for i in range(len(a)):
            p = e // a[-1]
            e -= a[-1]*p
            points += p

            e += a[i]

        return points
