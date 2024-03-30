class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def sw(k):
            total = 0
            count = Counter()

            left = 0
            for right in range(len(nums)):
                count[nums[right]] += 1

                while len(count) > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1

                total += right - left + 1

            return total

        # exactly K times = at most K times - at most K - 1 times
        return sw(k) - sw(k - 1)
