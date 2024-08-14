class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:

        while True:
            na = arr[:]
            for i in range(1, len(arr) - 1):
                if arr[i - 1] > arr[i] < arr[i + 1]:
                    na[i] += 1
                if arr[i - 1] < arr[i] > arr[i + 1]:
                    na[i] -= 1

            if na == arr:
                break

            arr = na

        return arr
