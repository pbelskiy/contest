class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = {(x, y): x**2 + y**2 for x, y in points}

        cp = []
        for closest in sorted(distances.items(), key=lambda k: k[1])[:k]:
            cp.append(closest[0])

        return cp
