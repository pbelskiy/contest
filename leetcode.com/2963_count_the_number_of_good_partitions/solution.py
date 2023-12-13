"""
Save in hasmap position of last occurance of each number,
then try to find minimal non overlaping interval.
"""
class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        last = {}
        for i in range(len(nums)):
            last[nums[i]] = i

        p = 0
        i = 0

        while i < len(nums):
            if i == last[nums[i]]:
                j = i
            else:
                j = last[nums[i]]

            # get max from range
            changed = True
            while changed:
                changed = False
                for k in range(i, j):
                    if last[nums[k]] > j:
                        j = last[nums[k]]
                        changed = True

            i = j + 1
            p += 1

        return (2**(p - 1)) % (10**9 + 7)
