class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []

        for x0, y0, r in queries:
            total = 0

            for x, y in points:
                if (x - x0)**2 + (y - y0)**2 <= r**2:
                    total += 1

            res.append(total)

        return res
