class Solution:
    def reverseByType(self, s: str) -> str:
        chars = []
        special = []

        for ch in s:
            if ch in string.ascii_letters:
                chars.append(ch)
            else:
                special.append(ch)

        ns = ''
        for ch in s:
            if ch in string.ascii_letters:
                ns += chars.pop()
            else:
                ns += special.pop()

        return ns

