class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = Counter(words)
        count = Counter()
        pal = Counter()

        for word in words:
            rev = word[::-1]
            if rev == word:
                pal[word] += 1
            else:
                count[word] = freq[rev]

        longest = 0
        used = False

        # join palindroms
        for _, v in pal.most_common():
            if v % 2 == 0:
                longest += v*2
            elif not used:
                longest += v*2
                used = True
            else:
                longest += (v-1)*2

        # join mirrored chunks
        for k, v in count.items():
            if count[k] > 0:
                rev = k[::-1]
                longest += min(count[k], count[rev])*4

                count[k] = 0
                count[rev] = 0

        return longest
