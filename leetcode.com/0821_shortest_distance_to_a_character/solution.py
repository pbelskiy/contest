class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        a = [float('inf')]*len(s)

        def mark(i):
            left = i - 1
            right = i + 1

            while left >= 0:
                a[left] = min(a[left], abs(left - i))
                left -= 1

            while right < len(s):
                a[right] = min(a[right], abs(right - i))
                right += 1

        for i in range(len(s)):
            if s[i] == c:
                a[i] = 0
                mark(i)

        return a
