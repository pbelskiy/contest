class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        left_sum = [sum(nums[:i]) for i in range(len(nums))]
        right_sum = [sum(nums[:i:-1]) for i in range(len(nums))]

        return [abs(left_sum[i] - right_sum[i]) for i in range(len(nums))]
