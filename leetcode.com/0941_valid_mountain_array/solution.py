class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        si = False
        sd = False

        i = 0

        while i + 1 < len(arr) and arr[i] < arr[i + 1]:
            i += 1
            si = True

        m = arr[i]
        i += 1

        while i < len(arr) and m > arr[i] and arr[i - 1] > arr[i]:
            i += 1
            sd = True

        return si and sd and i == len(arr)
