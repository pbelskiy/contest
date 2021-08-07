class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        matches = []

        for word in queries:
            p = 0
            matched = True
            for ch in pattern:
                сhu = ch.isupper()

                while p < len(word):
                    if word[p] == ch:
                        p += 1
                        break
                    elif сhu and word[p].isupper():
                        matched = False
                        break

                    p += 1
                else:
                    matched = False
                    break

            # check if there is upper in rest of word
            while p < len(word):
                if word[p].isupper():
                    matched = False
                    break
                p += 1

            matches.append(matched)

        return matches
