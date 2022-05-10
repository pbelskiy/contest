class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []

        for i in range(len(l)):
            a = sorted(nums[l[i]:r[i]+1])
            d = a[1] - a[0]

            for j in range(len(a) - 1):
                if a[j + 1] - a[j] != d:
                    res.append(False)
                    break
            else:
                res.append(True)

        return res
