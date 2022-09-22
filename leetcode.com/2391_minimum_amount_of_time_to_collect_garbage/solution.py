class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total = 0
        travel.insert(0, 0)

        for t in 'MPG':
            cost = 0

            for i, g in enumerate(garbage):
                count = g.count(t)
                if count:
                    total += count + travel[i] + cost
                    cost = 0
                else:
                    cost += travel[i]

        return total
