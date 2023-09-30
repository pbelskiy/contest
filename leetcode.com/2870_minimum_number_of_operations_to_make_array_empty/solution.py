class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        ops = 0

        for n in count.values():
            if n == 1:
                return -1

            p1 = (n // 3) - 1
            p2 = n - p1*3
            ops += p1 + p2 // 2

        return ops
