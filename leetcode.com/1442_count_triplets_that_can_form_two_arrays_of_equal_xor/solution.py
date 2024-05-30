class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        t = 0

        for i in range(len(arr)):
            a = 0
            for j in range(i + 1, len(arr)):
                a ^= arr[j - 1]
                b = 0
                for k in range(j, len(arr)):
                    b ^= arr[k]
                    if a == b:
                        t += 1

        return t
