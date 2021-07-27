class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = 0
        delta = 10**4
        length = len(nums)

        for i in range(length - 2):
            n = nums[i]
            left = i + 1
            right = length - 1

            while left < right:
                total = n + nums[left] + nums[right]

                if total > target:
                    right -= 1
                else:
                    left += 1

                _d = abs(target - total)
                if _d >= delta:
                    continue

                delta = _d
                closest = total

        return closest
