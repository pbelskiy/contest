class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_count = len(set(nums))

        total = 0
        for i in range(len(nums)):
            count = Counter()
            for j in range(i, len(nums)):
                count[nums[j]] += 1
                if len(count) == distinct_count:
                    total += 1

        return total
