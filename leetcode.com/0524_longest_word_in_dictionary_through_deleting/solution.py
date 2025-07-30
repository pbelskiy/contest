class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:

        def check(t):
            p = defaultdict(lambda: 0)
            i = 0

            for ch in t:
                # find next character using hashmap
                if not d[ch]:
                    return False

                # no more characters
                if p[ch] >= len(d[ch]):
                    return False

                while p[ch] < len(d[ch]) and d[ch][p[ch]] < i:
                    p[ch] += 1

                # needeed character before
                if p[ch] >= len(d[ch]) or d[ch][p[ch]] < i:
                    return False

                i = d[ch][p[ch]]
                p[ch] += 1

            return True

        # indices of first character occurrence
        d = defaultdict(list)
        for i in range(len(s)):
            d[s[i]].append(i)

        for t in sorted(dictionary, key=lambda t: (-len(t), t)):
            if check(t):
                return t

        return ''

