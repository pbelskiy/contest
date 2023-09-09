class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:

        @cache
        def is_prime(v):
            if v == 1:
                return False

            if v != 2 and v % 2 == 0:
                return False

            for n in range(2, v):
                if v % n == 0:
                    return False

            return True

        n = len(nums)
        target = []

        for d in range(n):
            target.append(nums[d][d])
            target.append(nums[d][n - d - 1])

        for v in sorted(target, reverse=True):
            if is_prime(v):
                return v

        return 0
