class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        nums = [abs(ord(a) - ord(b)) for a, b in zip(s, t)]

        left = 0
        curr_sum = 0
        max_count = 0

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum > maxCost:
                curr_sum -= nums[left]
                left += 1

            max_count = max(max_count, right - left + 1)

        return max_count
