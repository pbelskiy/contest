class Solution:
    def countPoints(self, rings: str) -> int:
        count = defaultdict(set)

        for i in range(0, len(rings) - 1, 2):
            count[rings[i + 1]].add(rings[i])

        return sum(1 for v in count.values() if len(v) == 3)
