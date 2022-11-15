class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        count = Counter(
            paragraph.replace('!', ' ')
                     .replace('?', ' ')
                     .replace('\'', ' ')
                     .replace(',', ' ')
                     .replace(';', ' ')
                     .replace('.', ' ')
                     .lower()
                     .split()
        )

        for word in count.most_common():
            if word[0] not in banned:
                return word[0]
