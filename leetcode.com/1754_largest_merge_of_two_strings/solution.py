class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        m = ''

        while i < len(word1) and j < len(word2):
            if word1[i:] > word2[j:]:
                m += word1[i]
                i += 1
            else:
                m += word2[j]
                j += 1

        return m + word1[i:] + word2[j:]
