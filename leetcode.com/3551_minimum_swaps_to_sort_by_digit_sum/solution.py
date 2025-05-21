"""
Sort array by criteria, then count number of needed swaps
of to reach sorted array.

TC: O(sort)
TC: O(sort)
"""
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        arr = sorted(nums, key=lambda v: (sum(map(int, str(v))), v))

        d = {n: i for i, n in enumerate(nums)}
        s = 0

        for i in range(len(nums)):
            if nums[i] == arr[i]:
                continue

            j = d[arr[i]]
            nums[i], nums[j] = nums[j], nums[i]

            d[nums[i]] = i
            d[nums[j]] = j

            s += 1

        return s

