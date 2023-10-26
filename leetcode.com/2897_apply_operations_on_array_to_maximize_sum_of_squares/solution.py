class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        # collect existed bits
        d = defaultdict(int)
        for n in nums:
            for i in range(n.bit_length()):
                if n & (1 << i):
                    d[i] += 1

        # build number using collected bits
        t = 0
        for _ in range(k):
            n = 0
            for i in d:
                if d[i] > 0:
                    n |= (1 << i)
                    d[i] -= 1

            t = (t + n**2) % (10**9 + 7)

        return t
