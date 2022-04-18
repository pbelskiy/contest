class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        a, b = None, None

        d1 = float('-inf')
        d2 = float('-inf')
        d3 = float('-inf')

        for i, s in enumerate(seats):
            if not s:
                continue

            if d1 == float('-inf'):
                d1 = i

            a, b = i, a
            if b is not None:
                d3 = max(d3, abs(a - b))

        d2 = len(seats) - 1 - a

        # from left || from right || middle
        return max(d1, d2, d3 // 2)
