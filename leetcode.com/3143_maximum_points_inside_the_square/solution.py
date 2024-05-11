"""

"""
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        count = defaultdict(list)

        for (y, x), t in zip(points, s):
            d = max(abs(x), abs(y))
            count[d].append(t)

        seen = set()

        for distance, tags in sorted(count.items()):
            if len(tags) != len(set(tags)):
                break
            if set(tags) & seen:
                break
            seen |= set(tags)

        return len(seen)
