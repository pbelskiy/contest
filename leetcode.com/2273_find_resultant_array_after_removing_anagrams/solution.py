class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        found = True
        while found:
            found = False
            for i in range(1, len(words)):
                if Counter(words[i - 1]) == Counter(words[i]):
                    words = words[:i] + words[i+1:]
                    found = True
                    break

        return words
