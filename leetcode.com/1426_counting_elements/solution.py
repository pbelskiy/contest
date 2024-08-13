class Solution:
    def countElements(self, arr: List[int]) -> int:
        s = set(arr)
        t = 0

        for n in arr:
            if n + 1 in s:
                t += 1

        return t
