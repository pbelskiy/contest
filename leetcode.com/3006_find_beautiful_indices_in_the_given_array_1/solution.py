class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        ai, bi, = [], []
        for src, arr, i in ((a, ai, 0), (b, bi, 0)):
            while True:
                i = s.find(src, i)
                if i == -1:
                    break
                arr.append(i)
                i += 1

        indices = set()
        # find final indices
        for i in ai:
            for j in bi:
                if abs(i - j) <= k:
                    indices.add(i)
                    break

        return sorted(indices)
