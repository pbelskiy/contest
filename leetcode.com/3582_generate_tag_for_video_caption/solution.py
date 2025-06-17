class Solution:
    def generateTag(self, caption: str) -> str:
        s = '#'

        for i, w in enumerate(caption.split()):
            if i == 0:
                s += w.lower()
            else:
                s += w.capitalize()

        return s[:100]

