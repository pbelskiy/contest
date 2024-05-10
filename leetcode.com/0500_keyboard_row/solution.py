class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        results = []

        for word in words:
            for row in ("qwertyuiop", "asdfghjkl", "zxcvbnm"):
                if set(word.lower()) - set(row):
                    continue

                results.append(word)
                break

        return results
