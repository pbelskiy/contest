class Solution:
    def minOperations(self, s: str) -> int:
        for ch in sorted(set(s)):
            if ch == 'a':
                continue
            return ord('z') - ord(ch) + 1

        return 0

