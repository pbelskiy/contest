class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        t = 0
        for n, f in Counter(nums).items():
            if f % k == 0:
                t += n*f
        return t

