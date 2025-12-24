class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count, dup = defaultdict(int), set()

        for n in nums:
            count[n] += 1
            if count[n] > 1:
                dup.add(n)

        left = 0
        while dup:
            for i in range(left, min(left + 3, len(nums))):
                count[nums[i]] -= 1

                if count[nums[i]] == 1 and nums[i] in dup:
                    dup.remove(nums[i])

            left += 3

        return left // 3
 
