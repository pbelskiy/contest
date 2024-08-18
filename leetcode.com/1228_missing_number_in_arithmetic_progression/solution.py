class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        arr.sort()
        x = min([arr[i + 1] - arr[i] for i in range(len(arr) - 1)])

        s = set(arr)
        for n in arr:
            if n + x not in s:
                return n + x

        return arr[0]
