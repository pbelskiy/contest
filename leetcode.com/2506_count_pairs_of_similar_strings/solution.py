class Solution:
    def similarPairs(self, words: List[str]) -> int:
        total = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not (set(words[i]) ^ set(words[j])):
                    total += 1

        return total
