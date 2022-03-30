class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:

        def get(a, s):
            total = 0

            for i in range(s, len(a), 2):
                if i - 1 >= 0 and a[i - 1] >= a[i]:
                    d = a[i - 1] - a[i] + 1
                    a[i - 1] -= d
                    total += d

                if i + 1 < len(a) and a[i + 1] >= a[i]:
                    d = a[i + 1] - a[i] + 1
                    a[i + 1] -= d
                    total += d

            return total

        return min(get(nums[:], 0), get(nums[:], 1))
