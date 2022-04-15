class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        i = 0
        while i < len(arr):
            for p in pieces:
                j = 0
                while j < len(p) and arr[i] == p[j]:
                    i += 1
                    j += 1

                if j > 0:
                    break
            else:
                break

        return i == len(arr)
