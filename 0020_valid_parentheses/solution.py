class Solution:
    def isValid(self, s: str) -> bool:
        l = []

        try:
            for ch in s:
                if ch in ('(', '{', '['):
                    l.append(ch)
                    continue

                if ch == ')':
                    if l.pop() != '(':
                        return False
                elif ch == '}':
                    if l.pop() != '{':
                        return False
                elif ch == ']':
                    if l.pop() != '[':
                        return False
        except IndexError:
            return False

        return len(l) == 0
