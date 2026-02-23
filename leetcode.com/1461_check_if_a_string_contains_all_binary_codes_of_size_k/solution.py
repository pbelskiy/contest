class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        u = set()

        for code in range(2**k):
            u.add(bin(code)[2:].rjust(k, '0'))

        left = 0
        for right in range(k, len(s) + 1):
            key = s[left:right]
            if key in u:
                u.remove(key)
            left += 1

        return len(u) == 0

