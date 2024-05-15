class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(' ')
        if spaces == 0:
            return text

        words = list(filter(lambda s: s, text.split(' ')))

        if len(words) == 1:
            d, m = 0, spaces
        else:
            d, m = divmod(spaces, len(words) - 1)

        s = ''
        for word in words:
            s += word + ' '*d

        return s.rstrip() + ' '*m
