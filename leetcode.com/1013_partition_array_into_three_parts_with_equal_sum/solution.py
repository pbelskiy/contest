class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s = sum(arr)
        if s % 3 == 1:
            return False

        t = s // 3

        s1 = 0
        for i in range(len(arr) - 2):
            s1 += arr[i]
            if s1 == t:
                s2 = 0
                for j in range(i + 1, len(arr) - 1):
                    s2 += arr[j]
                    if s1 == s2 and s - s1 - s2 == s1:
                        return True

        return False
