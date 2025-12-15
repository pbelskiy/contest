"""
Find increasing sequences, and use math.

TC: O(N)
SC: O(1)
"""
class Solution:
    def getDescentPeriods(self, a: List[int]) -> int:
        a += [10**10]  # for convenient processing last element

        t = 0
        n = 1
        for i in range(1, len(a)):
            if a[i] - a[i - 1] == -1:
                n += 1
            else:
                t += n * (n + 1) // 2
                n = 1

        return t

