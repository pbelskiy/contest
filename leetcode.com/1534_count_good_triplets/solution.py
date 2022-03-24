class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        total = 0
        n = len(arr)

        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    if not (i < j < k):
                        continue

                    if abs(arr[i] - arr[j]) > a:
                        continue

                    if abs(arr[j] - arr[k]) > b:
                        continue

                    if abs(arr[i] - arr[k]) > c:
                        continue

                    total += 1

        return total
