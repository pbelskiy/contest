class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = []
        s = 0

        for n in nums:
            s += n
            prefix.append(s)

        total = 0

        for i in range(len(prefix) - 1):
            a = prefix[i]
            b = prefix[-1] - a

            if a >= b:
                total += 1

        return total
