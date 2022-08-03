class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        t = 1
        a = sorted([d / s for d, s in zip(dist, speed)])

        for i in range(1, len(a)):
            if a[i] <= t:
                return i
            t += 1

        return len(a)
