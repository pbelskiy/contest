class Solution:
    def beautySum(self, s: str) -> int:

        @cache
        def get_beauty(s):
            most_common = Counter(s).most_common()
            return most_common[0][1] - most_common[-1][1]

        t = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                t += get_beauty(s[i:j+1])

        return t
