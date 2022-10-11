class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(set(nums)) < 3:
            return False

        n = len(nums)
        length = [1] * n

        for k in range(n):
            length[k] = 1

            for i in range(k):
                if nums[i] < nums[k]:
                    length[k] = max(length[k], length[i] + 1)

                    if length[k] >= 3:
                        return True

        return False
