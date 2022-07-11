class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        a = [nums[0]]
        for n in nums:
            if n != a[-1]:
                a.append(n)

        total = 0
        for i in range(1, len(a) - 1):
            if a[i - 1] < a[i] > a[i + 1]:
                total += 1

            if a[i - 1] > a[i] < a[i + 1]:
                total += 1

        return total
