class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        arrays.sort(key=len)

        res = []

        for n in arrays[0]:

            for arr in arrays[1:]:
                i = bisect.bisect_left(arr, n)
                if i >= len(arr) or arr[i] != n:
                    break
            else:
                res.append(n)

        return res
