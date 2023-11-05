class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        d = set(range(n)) - {b for _, b in edges}
        if len(d) == 1:
            return next(iter(d))
        return -1
