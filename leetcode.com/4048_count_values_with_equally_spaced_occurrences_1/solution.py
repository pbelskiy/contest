class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        t = 0
        d = defaultdict(list)

        for i in range(len(nums)):
            d[nums[i]].append(i)

        for _, v in d.items():
            if len(v) != 3:
                continue

            i1, i2, i3 = v

            if i2 - i1 == i3 - i2:
                t += 1

        return t

