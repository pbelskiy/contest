class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        t = 0
        a = []
        p = 0

        for i in range(len(arr)):
            a.append(arr[i])

            if sorted(a) == list(range(p, i + 1)):
                a = []
                p = i + 1
                t += 1

        return t
