class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        deltas = {}

        for i, n in enumerate(nums):
            x = target - n
            if x in deltas:
                return [i, deltas[x]]

            deltas[n] = i
