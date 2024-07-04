class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        t = 0

        for i in range(len(nums)):
            _max = _min = nums[i]
            for j in range(i, len(nums)):
                _max = max(_max, nums[j])
                _min = min(_min, nums[j])
                t += _max - _min

        return t
