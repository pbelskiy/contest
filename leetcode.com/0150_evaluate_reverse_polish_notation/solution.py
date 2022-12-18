class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for t in tokens:
            try:
                s.append(int(t))
            except ValueError:
                ...
            else:
                continue

            b = s.pop()
            a = s.pop()

            if t == '+':
                s.append(a + b)
            elif t == '-':
                s.append(a - b)
            elif t == '*':
                s.append(a * b)
            else:
                s.append(int(a / b))

        return s[0]
