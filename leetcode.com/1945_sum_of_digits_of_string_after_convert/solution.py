class Solution:
    def getLucky(self, s: str, k: int) -> int:
        v = ''.join(map(str, [ord(ch) - ord('a') + 1 for ch in s]))

        for _ in range(k):
            v = sum([int(ch) for ch in str(v)])

        return v
