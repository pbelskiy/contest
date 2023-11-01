"""
Inverse our condition to simplify problem.

total = bad + good
bad = total - good
good = i < j and j - i == nums[j] - nums[i].

=> j - i == nums[j] - nums[i]
=> j - nums[j] == i - nums[i]

SC: O(N)
TC: O(N)
"""
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for i, n in enumerate(nums):
            count[i - n] += 1

        total = math.comb(len(nums), 2)
        good = 0

        for v in count.values():
            good += math.comb(v, 2)

        return total - good
