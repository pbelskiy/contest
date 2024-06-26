class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr) - m*k + 1):
            for j in range(m):
                if len({arr[i+d*m+j] for d in range(k)}) != 1:
                    break
            else:
                return True

        return False
