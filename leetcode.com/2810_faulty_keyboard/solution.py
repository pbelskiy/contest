class Solution:
    def finalString(self, s: str) -> str:
        a = []

        for ch in s:
            if ch == 'i':
                a.reverse()
            else:
                a.append(ch)

        return ''.join(a)
