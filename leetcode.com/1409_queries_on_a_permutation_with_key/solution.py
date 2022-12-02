class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = deque(list(range(1, m + 1)))
        r = []

        for v in queries:
            i = p.index(v)
            p.remove(v)
            p.appendleft(v)
            r.append(i)

        return r
