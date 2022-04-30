class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefix_sum = []

        v = 0
        for n in nums:
            v += n
            prefix_sum.append(v)

        index = 0
        diff_min = float('inf')

        for i in range(len(prefix_sum)):
            a = (prefix_sum[i]) // (i + 1)

            if len(prefix_sum) - i - 1 != 0:
                b = (prefix_sum[-1] - prefix_sum[i]) // (len(prefix_sum) - i - 1)
            else:
                b = 0

            d = abs(a - b)
            if d < diff_min:
                diff_min = d
                index = i

        return index
