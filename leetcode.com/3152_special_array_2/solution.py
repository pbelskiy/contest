class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # form a list of ranges of special arrays
        s = []
        last = 0
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                s.append([last, i])
                last = i + 1
        s.append([last, len(nums) - 1])

        # using bisect check if query in some of special array
        r = []
        for left, right in queries:

            lo, hi = 0, len(s) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                i, j = s[mid]

                if i <= left <= right <= j:
                    r.append(True)
                    break

                if i > right:
                    hi = mid - 1
                else:
                    lo = mid + 1

            else:
                r.append(False)

        return r
