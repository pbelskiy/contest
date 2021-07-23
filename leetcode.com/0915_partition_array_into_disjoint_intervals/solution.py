from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        # intuitive answer
        # while max(nums[:left]) > min(nums[left:]):
        #     left += 1

        maximum = [0] * len(nums)
        minimum = [0] * len(nums)

        _max = 0
        for i in range(len(nums) - 1):
            _max = max(_max, nums[i])
            maximum[i] = _max

        _min = 10**6+1
        for i in range(len(nums) - 1, -1, -1):
            _min = min(_min, nums[i])
            minimum[i] = _min

        left = 1
        while maximum[left - 1] > minimum[left]:
            left += 1

        return left


cases = (
    ([1, 1], 1),
    ([1, 2, 5, 3, 10], 1),
    ([5, 0, 3, 8, 6], 3),
    ([1, 1, 1, 0, 6, 12], 4),
    ([26, 51, 40, 58, 42, 76, 30, 48, 79, 91], 1),
    ([90, 47, 69, 10, 43, 92, 31, 73, 61, 97], 9),
)

for tc, answer in cases:
    print(Solution().partitionDisjoint(tc), answer)
