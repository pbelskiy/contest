class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        total = 0
        for i in range(left, right + 1):
            if set([words[i][0], words[i][-1]]).issubset({'a', 'e', 'i', 'o', 'u'}):
                total += 1

        return total
