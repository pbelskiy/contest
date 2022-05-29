class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        total = 0

        for i in range(len(word)):
            for j in range(i + 1, len(word)):
                if set(word[i:j+1]) == vowels:
                    total += 1

        return total
