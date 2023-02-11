class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        for n in range(1, (len(sequence) // len(word) + 2)):
            if word*n not in sequence:
                return n - 1

        return 0
