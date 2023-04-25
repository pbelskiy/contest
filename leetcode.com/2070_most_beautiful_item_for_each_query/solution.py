class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda t: (t[0], -t[1]))

        for i in range(1, len(items)):
            items[i][1] = max(items[i - 1][1], items[i][1])

        res = []

        for p in queries:
            index = bisect.bisect(items, p, key=lambda t: t[0]) - 1
            if items[index][0] > p:
                res.append(0)
            else:
                res.append(items[index][1])

        return res
