class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        h = []
        for n in nums:
            heappush(h, -n)

        s = 0
        while k > 0:
            n = heappop(h)
            s += -n
            heappush(h, n // 3)
            k -= 1

        return s
