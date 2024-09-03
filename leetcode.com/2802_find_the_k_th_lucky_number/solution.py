class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        s = ""
        k += 1

        while k > 1:
            d, m = divmod(k, 2)
            if m == 1:
                s += "7"
            else:
                s += "4"

            k = d

        return s[::-1]
