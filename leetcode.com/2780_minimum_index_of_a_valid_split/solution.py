"""
Sliding window

SC: O(N)
TC: O(N)
"""
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        left = Counter()
        right = Counter(nums)

        d = right.most_common(1)[0][0]

        for i in range(len(nums)):
            left[nums[i]] += 1
            right[nums[i]] -= 1

            # check left array
            left_size = i + 1
            if left[d] <= left_size // 2:
                continue

            # check right array
            right_size = len(nums) - i - 1
            if right[d] <= right_size // 2:
                continue

            return i

        return -1

