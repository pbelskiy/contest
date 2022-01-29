class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return '0'

        nums.sort(key=functools.cmp_to_key(lambda n1, n2: -int(str(n1) + str(n2) >= str(n2) + str(n1))))
        return ''.join(map(str, nums))
