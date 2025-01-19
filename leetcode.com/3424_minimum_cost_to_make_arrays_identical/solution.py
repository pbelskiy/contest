class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        m = 0

        for a, b in zip(arr, brr):
            m += abs(a - b)

        arr.sort()
        brr.sort()

        t = 0
        for a, b in zip(arr, brr):
            t += abs(a - b)

        return min(m, t + k)
