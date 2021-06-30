class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = []
        for m in matrix:
            l.extend(m)

        l.sort()
        return l[k-1]
