class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False

        if sorted(Counter(word1).values()) != sorted(Counter(word2).values()):
            return False

        return True
