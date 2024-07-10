"""
Greedy, use frequency of frequency to decide if
prefix is good.

TC: O(N)
SC: O(N)
"""
def check(count, cc):
    if len(count) == 1:
        return True

    if len(cc) == 1 and list(count.values())[0] == 1:
        return True

    if len(cc) == 2:
        if cc[max(cc)] == 1 and max(cc) - min(cc) == 1:
            return True

        if cc[min(cc)] == 1 and min(cc) == 1:
            return True

    return False


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        m = 0
        count = Counter()
        cc = Counter()

        for i in range(len(nums)):
            if count[nums[i]] > 0:
                cc[count[nums[i]]] -= 1
                if cc[count[nums[i]]] == 0:
                    del cc[count[nums[i]]]

            count[nums[i]] += 1
            cc[count[nums[i]]] += 1

            if check(count, cc):
                m = max(m, i + 1)

        return m
