class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word += 'X'
        abbr += 'X'

        # expand
        ns = ''
        d = ''

        for ch in abbr:
            if ch.isdigit():
                d += ch
            elif d.startswith('0'):
                return False
            elif d and int(d) > len(word):
                return False
            elif d:
                ns += '*'*int(d) + ch
                d = ''
            else:
                ns += ch

        if len(word) != len(ns):
            return False

        for a, b in zip(word, ns):
            if b == '*':
                continue

            if a != b:
                return False

        return True
