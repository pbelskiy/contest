class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        total = 0

        for w, c in Counter(words).items():
            i = j = 0

            while i < len(s) and j < len(w):

                if s[i] == w[j]:
                    i += 1
                    j += 1
                else:
                    i += 1

            if j == len(w):
                total += c

        return total
