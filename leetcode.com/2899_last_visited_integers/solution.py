class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        nums = []
        res = []
        idx = -1

        for w in words:
            if w != 'prev':
                nums.append(int(w))
                idx = len(nums) - 1
                continue

            if idx < 0:
                res.append(-1)
                continue

            res.append(nums[idx])
            idx -= 1

        return res
