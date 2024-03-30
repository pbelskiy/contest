class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        count, best = Counter(), float('inf')

        def set_bits(n, v):
            for i in range(32):
                if n & (1 << i):
                    count[i] += v

        def get_total():
            t = 0
            for k, v in count.items():
                if v > 0:
                    t |= (1 << k)

            return t

        left = 0
        for right in range(len(nums)):
            set_bits(nums[right], +1)

            while get_total() >= k:
                best = min(best, right - left + 1)

                if left >= right:
                    break
                set_bits(nums[left], -1)
                left += 1

        if best == float('inf'):
            return -1

        return best
