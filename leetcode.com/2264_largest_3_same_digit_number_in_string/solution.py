class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best = ""

        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                best = max(best, num[i]*3)

        return best
