class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [t[1] for t in sorted([(r.count(1), i) for i, r in enumerate(mat)])][:k]
