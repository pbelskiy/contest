"""
Apply binary search here, idea is that we continue search on
left or right slice of mid, if len of part is not aligned of 2.

Example: [1,1,2,2,3]

Middle index is 2 (=2), neares same value is on index 3, so we
can continue our binary search in right side of indexes 4..4.

TC: O(lgN)
SC: O(1)
"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if mid - 1 >= 0 and nums[mid] == nums[mid - 1]:
                if (left + mid + 1) % 2 == 1:
                    right = mid - 2
                else:
                    left = mid + 1

            elif mid + 1 < len(nums) and nums[mid] == nums[mid + 1]:
                if (right - mid + 1) % 2 == 0:
                    right = mid - 1
                else:
                    left = mid + 2

            else:
                return nums[mid]
