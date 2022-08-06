class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        count = Counter()

        for v, w in items1:
            count[v] += w

        for v, w in items2:
            count[v] += w

        a = []
        for k, v in count.items():
            a.append([k, v])

        a.sort(key=lambda t: t[0])
        return a
