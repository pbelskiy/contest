class Solution:
    def splitArray(self, nums: List[int]) -> int:

        def is_prime(n):
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True
        
        def get_primes():
            return [n for n in range(2, len(nums)) if is_prime(n)]

        p = set(get_primes())
        a = 0
        b = 0

        for i in range(len(nums)):
            if i in p:
                a += nums[i]
            else:
                b += nums[i]

        return abs(a - b)

