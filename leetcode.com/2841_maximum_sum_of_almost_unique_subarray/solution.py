class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        result = 0
        window = Counter()
        left = 0
        total = 0

        for right in range(len(nums)):
            window[nums[right]] += 1
            total += nums[right]

            if right - left + 1 < k:
                continue

            if len(window) >= m:
                result = max(result, total)

            window[nums[left]] -= 1
            total -= nums[left]
            left += 1

            if window[nums[left - 1]] == 0:
                del window[nums[left - 1]]

        return result
