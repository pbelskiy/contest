class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def sw(k):
            total, count = 0, 0

            left = 0
            for right in range(len(nums)):
                count += nums[right] % 2

                while count > k:
                    count -= nums[left] % 2
                    left += 1

                total += right - left + 1

            return total

        # exactly K times = at most K times - at most K - 1 times
        return sw(k) - sw(k - 1)
