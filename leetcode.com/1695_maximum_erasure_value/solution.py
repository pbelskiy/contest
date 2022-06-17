class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        count = set()
        max_score = cur_score = 0
        left = right = 0

        while right < len(nums):

            while nums[right] in count:
                count.remove(nums[left])
                cur_score -= nums[left]
                max_score = max(max_score, cur_score)
                left += 1

            count.add(nums[right])
            cur_score += nums[right]
            max_score = max(max_score, cur_score)
            right += 1

        return max_score
