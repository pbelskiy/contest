class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        r = []

        for i in range(len(nums) - k + 1):
            a = nums[i:i+k]
            sa = sorted(a)
            if a != sa:
                r.append(-1)
                continue

            for j in range(len(sa) - 1):
                if sa[j] + 1 != sa[j + 1]:
                    r.append(-1)
                    break
            else:
                r.append(sa[-1])

        return r
