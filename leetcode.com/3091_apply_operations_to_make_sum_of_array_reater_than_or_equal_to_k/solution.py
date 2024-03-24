class Solution:
    def minOperations(self, k: int) -> int:
        best = float('inf')
        for n in range(1, 10**5):
            length = math.ceil(k / n)     # length of array of [n, n, ...]
            ops = (length - 1) + (n - 1)  # operations to make such array
            if ops > best:
                break
            best = ops

        return best
