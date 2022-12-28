class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        h, s = [], 0

        for n in piles:
            heappush(h, -n)
            s += n

        for _ in range(k):
            n = heappop(h)
            d = math.ceil(n / 2)
            s += d
            heappush(h, n - d)

        return s
