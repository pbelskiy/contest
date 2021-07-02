class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        def a_closer_b(a, b):
            return (abs(a - x) < abs(b - x)) or (abs(a - x) == abs(b - x) and a < b)

        if x >= arr[-1]:
            return arr[len(arr)-k:]

        if x <= arr[0]:
            return arr[:k]

        for i, n in enumerate(arr):
            if n >= x:
                break

        l = i
        r = i
        d = 0

        while r - l != k:
            try:
                a = arr[l - 1]
                b = arr[r]
            except IndexError:
                d = 1

            if (a_closer_b(a, b) and l > 0) or r > len(arr) - 1:
                l -= 1
            elif r < len(arr):
                r += 1
            else:
                break

        return arr[l:r+d]
