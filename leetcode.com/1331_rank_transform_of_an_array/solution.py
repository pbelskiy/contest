class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {i: r for r, i in enumerate(sorted(set(arr)), start=1)}
        return [d[i] for i in arr]