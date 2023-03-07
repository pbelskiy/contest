class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.extend([0, 10**10])
        nums.sort()

        t = 0
        for i in range(len(nums) - 1):
            a, b = nums[i], nums[i + 1]
            d = b - a - 1
            if d < 1:
                continue

            p = min(d, k)
            a, b = a + 1, a + p
            t += (a + b) * (b - a + 1) // 2

            k -= p
            if k == 0:
                break

        return t
