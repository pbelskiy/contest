class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        best = 0
        count = Counter()

        for right in range(len(nums)):
            count[nums[right]] += 1

            while max(count) - min(count) > limit:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1

            best = max(best, right - left + 1)

        return best
