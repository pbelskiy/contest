class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        def solve(i, d, a):
            while 0 <= i < len(a):
                if a[i] == 0:
                    i += d
                    continue

                a[i] -= 1

                # reverse
                if d == -1:
                    d = +1
                else:
                    d = -1

                i += d

            return sum(a) == 0

        t = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                if solve(i, -1, nums[:]):
                    t += 1

                if  solve(i, +1, nums[:]):
                    t += 1

        return t
