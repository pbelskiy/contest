"""
To improve performance of brute force we do it position by
position, since total numbers of is limit by (0~9), so it
will be in worse case 10**2 for each position.

TC: O(N)
SC: O(N)
"""
class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        t = 0
        w = len(str(nums[0]))

        # calcualte by position
        for i in range(w):
            count = Counter([str(nums[j])[i] for j in range(len(nums))])
            digits = list(count)

            for j in range(len(digits)):
                for k in range(j + 1, len(digits)):
                    if digits[j] == digits[k]:
                        continue

                    t += count[digits[j]] * count[digits[k]]

        return t
