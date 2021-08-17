class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missed = []
        last = arr[-1]

        pos = 0

        for n in range(1, last + 1):
            if n == arr[pos]:
                pos += 1
            else:
                missed.append(n)

        missed += list(range(last + 1, last + k + 1))
        return missed[k - 1]
